<p>//Computer Systems and Networks- IoT Assignment 2 </p>
<h1>Daily Doser QR Code Scanner Project</h1>

<h2>Áine Phelan -W20114761</h2>


<h4><em>INTRODUCTION</em></h4>

<p>The following README contains documentation on how to interact with the Daily Doser IoT Assignment.
   This is a more scaled back version that was initially pitched to fit into the time frame. I hope to continue work on it it in 2026. The project follows a client server architecture.
   To summarise, the main idea of the project and the stage it is at at present is that using the Raspberry Pi Camera Module captures a QR Code from
   an image using pyzbar and Picamera2. The data is then transmitted as a JSON payload via HTTP Post to a the Flask API. This then processes it and updates the Daily Doser webpage
   and displays the Medication name and puts a timestamp on it also. The webpage is at a basic stage just displaying JSON payloads at the moment. 
</p>


<h4><em>HOW TO RUN</em></h4>

<ul>
<li>In a terminal, access on Raspberry Pi, access the project folder /daily_doser_iot_project. </li>
<li>Access the installed virtual machine by running source ./.venv/bin/activate </li>
<li>Serve Flask API by running python backend/sense_api.py. Select the live web address at http://192.168.0.17:5000.</li>
<li>Open up another tab in selected terminal, Powershell etc, key into the Raspberry Pi and project folder once more whilst leaving the Flask API running.</li>
<li>Access virtual machine in this tab also and run the Camera/QR Code Scanning python script by running the command: python pi_client/qr_code_scan.py </li>
<li>Hold up a QR CODE that already has a medicine name on it, the terminal will show you initially if capture was successful. </li>
<li>Refresh the Daily Doser Webpage and the Medication information and Timestamp will appear on the page. There is a small cooldown before another QR Code can be captured. </li>
</ul>

<h4><em> LINKS, DOCUMENTATION AND SOURCES </em></h4>

<ul>
<li>GITHUB REPO LINK:https://github.com/ainephelan365/daily_doser_iot_project.git</li>
<li>PYZBAR DOCUMENTATION: https://pypi.org/project/pyzbar/ </li>
<li>QR CODE DETECTION SOURCES: https://note.nkmk.me/en/python-pyzbar-barcode-qrcode/, https://www.youtube.com/watch?v=zetQzP12fSQ (mainly used for the learning/implementation of decoding)</li>
<li>FLASK DOCUMENTATION: https://flask.palletsprojects.com/en/stable/api/ </li>
<li>FLASK IMPLEMENTATION/SOURCE: HDip Computer Science Labs, Week 9 and Week 10.. </li>
<li>RASPBERRY PI CAMERA SETUP/IMPLEMENTATION:HDip Computer Science Labs, Week 10. </li>
<li>HTML, CSS AND BULMA FOR WEBPAGE: Referenced Weather App Assignment in Web Development 2, github link:https://github.com/ainephelan365/Web_Dev_Assignment_2_final.git </li>
<li>VIRTUAL ENVIRONMENT CREATION/DOCUMENTATION: https://docs.python.org/3/library/venv.html , Also followed HDip Computer Science Lab Week 9 lab 1- Pip and Python Virtual Environments.
</ul>



<h4><em>CONTACT INFORMATION</em></h4>

<p>For further information, guidance and correspondence, contact myself Áine on github <em>ainephelan365</em> or send a message on Slack!</p>
<p>Follow the Instagram page for more updates, content and posts! https://www.instagram.com/daily_doser_project/   </p>
