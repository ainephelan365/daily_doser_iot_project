
# QR Code Scanner Script
# Use Raspberry Pi camera to capture images
# Decodes the qr code in the image using pyzbar and sends to Flask HTTP API
# Sites used for reference mainly for pyzbar and decode are linked in README

#!/usr/bin/env python3
from PIL import Image
from pyzbar.pyzbar import decode
from picamera2 import Picamera2
from time import sleep, time
from datetime import datetime
import requests

# Api URL
API_URL = "http://127.0.0.1:5000/api/dose"
IMAGE_PATH = "/tmp/qr.jpg"

#To stop the API from being overloaded
LAST_QR = None
LAST_SENT = 0
COOLDOWN_SECONDS = 4

#Captures image
def capture_photo(picam2: Picamera2):
    print("Capturing QR Code photo!")
    picam2.capture_file(IMAGE_PATH)


def decoding_qrcode_image():
    img = Image.open(IMAGE_PATH)
    results = decode(img)

    if not results:
        return None

    return results[0].data.decode("utf-8").strip()


def send_to_api(qr_text_name: str):
    payload = {
        "medication": qr_text_name,
        "timestamp": datetime.now().isoformat(),
        "dose_taken": True
    }

    response = requests.post(API_URL, json=payload, timeout=4)
    print("POST", response.status_code, response.text)


#Booting up camera
def main():
    global LAST_QR, LAST_SENT

    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration())
    picam2.start()

    print("Booting up Pi Camera")
    sleep(3)

    print("QR Code Scanner currently running...")
    print("Sending JSON Event to:", API_URL)

    try:
       while True:
            capture_photo(picam2)
            qr_text_name = decoding_qrcode_image()

            if qr_text_name:
                now = time()
                if (qr_text_name != LAST_QR) or (now - LAST_SENT > COOLDOWN_SECONDS):
                    print("QR CODE DETECTED:", qr_text_name)
                    send_to_api(qr_text_name)
                    LAST_QR = qr_text_name
                    LAST_SENT = now
                else:
                    print("QR Code scanned too soon please wait....")
            else:
                print("No QR Code found")

            sleep(0.5)

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        picam2.stop()



if __name__ == "__main__":
    main()

