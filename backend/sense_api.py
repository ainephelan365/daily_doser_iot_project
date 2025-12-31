from flask import Flask, request, render_template
from datetime import datetime

# Creating Flask App
app = Flask(__name__)

# in-memory data storage 
last_event = {
    "medication": "None",
    "timestamp": "Not available"
}

# Base webpage interface

@app.route('/')
def index():
    """
    Render the device status web page.
    """
    return render_template(
        'status.html',
        medication=last_event["medication"],
        timestamp=last_event["timestamp"]
    )


# API Route that receives dose recordings via HTTP

@app.route('/api/dose', methods=['POST'])
def api_dose():
    """
    Receiving medication dosage record as a JSON file.
    Example:
    {
        "medication": "Spironolactone",
        "timestamp": "2025-11-31T12:00:00",
        "dose_taken": true
    }
    """

    # Read the JSON data sent by client
    data = request.get_json() or {}

    # Update in-memory store
    last_event["medication"] = data.get("medication", "Unknown")
    last_event["timestamp"] = data.get(
        "timestamp",
        datetime.now().isoformat()
    )

    # Return JSON response with HTTP OK (200)
    return {"status": "received"}, 200

# App entry point for running Flask on my Pi
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",  # Allow access from other devices
        port=5000

    )

