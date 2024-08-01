
import os
import psutil
import smtplib
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'b90737530@gmail.com'  # Replace with your email
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')  # Get password from environment variable
EMAIL_FROM = 'b90737530@gmail.com'  # Replace with your email
EMAIL_TO = 'alert_recipient@example.com'  # Replace with the recipient's email
EMAIL_SUBJECT = 'System Alert'

# Monitoring thresholds
DISK_USAGE_THRESHOLD = 80  # in percent
CPU_USAGE_THRESHOLD = 90  # in percent

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            print("Alert sent successfully.")
    except Exception as e:
        print(f"Failed to send alert: {e}")

def check_disk_space():
    usage = psutil.disk_usage('/')
    if usage.percent > DISK_USAGE_THRESHOLD:
        message = f"Warning: Disk usage is at {usage.percent}%"
        send_alert("Disk Space Alert", message)

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_USAGE_THRESHOLD:
        message = f"Warning: CPU usage is at {usage}%"
        send_alert("CPU Usage Alert", message)

if __name__ == "__main__":
    check_disk_space()
    check_cpu_usage()
