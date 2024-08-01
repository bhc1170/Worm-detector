import os
import psutil
import smtplib
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'b90737530@gmail.com'
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')  # Use the app-specific password from environment variable
EMAIL_FROM = 'b90737530@gmail.com'
EMAIL_TO = 'b90737530@gmail.com'
EMAIL_SUBJECT = 'System Alert'

# Monitoring thresholds (adjust as needed)
DISK_USAGE_THRESHOLD = 10  # Lower for testing
CPU_USAGE_THRESHOLD = 1    # Lower for testing

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        print("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.set_debuglevel(1)  # Enable debug output
            server.starttls()
            print("Logging in with username:", SMTP_USERNAME)
            print("Logging in with password:", SMTP_PASSWORD)
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            print("Sending email...")
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            print("Alert sent successfully.")
    except Exception as e:
        print(f"Failed to send alert: {e}")

def check_disk_space():
    usage = psutil.disk_usage('/')
    print("Disk usage: ", usage.percent)  # Debug print statement
    if usage.percent > DISK_USAGE_THRESHOLD:
        message = f"Warning: Disk usage is at {usage.percent}%"
        send_alert("Disk Space Alert", message)
    else:
        print("Disk usage is within limits.")

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    print("CPU usage: ", usage)  # Debug print statement
    if usage > CPU_USAGE_THRESHOLD:
        message = f"Warning: CPU usage is at {usage}%"
        send_alert("CPU Usage Alert", message)
    else:
        print("CPU usage is within limits.")

if __name__ == "__main__":
    print("Starting system monitor...")
    print("Using SMTP_PASSWORD:", SMTP_PASSWORD)  # Debug print statement to check the password
    check_disk_space()
    check_cpu_usage()
