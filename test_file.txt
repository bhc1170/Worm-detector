import os
import psutil
import smtplib
from email.mime.text import MIMEText
import logging
from sklearn.ensemble import IsolationForest
import yara
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'b90737530@gmail.com'
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAIL_FROM = 'b90737530@gmail.com'
EMAIL_TO = 'b90737530@gmail.com'
EMAIL_SUBJECT = 'System Alert'

# Monitoring thresholds
DISK_USAGE_THRESHOLD = 10
CPU_USAGE_THRESHOLD = 1

# Logging configuration
logging.basicConfig(filename='system_monitor.log', level=logging.INFO)

# YARA rules file
YARA_RULES_FILE = 'example_rule.yar'

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        print("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.set_debuglevel(1)
            server.starttls()
            print("Logging in with username:", SMTP_USERNAME)
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            print("Sending email...")
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            print("Alert sent successfully.")
    except Exception as e:
        print(f"Failed to send alert: {e}")

def check_disk_space():
    usage = psutil.disk_usage('/')
    logging.info(f"Disk usage: {usage.percent}%")
    if usage.percent > DISK_USAGE_THRESHOLD:
        message = f"Warning: Disk usage is at {usage.percent}%"
        send_alert("Disk Space Alert", message)

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    logging.info(f"CPU usage: {usage}%")
    if usage > CPU_USAGE_THRESHOLD:
        message = f"Warning: CPU usage is at {usage}%"
        send_alert("CPU Usage Alert", message)

def detect_fraud(data):
    clf = IsolationForest(random_state=0).fit(data)
    outliers = clf.predict(data)
    if -1 in outliers:
        send_alert("Fraud Detection Alert", "Potential fraud detected.")
    else:
        print("No fraud detected.")

def scan_for_malware():
    try:
        rules = yara.compile(filepath=YARA_RULES_FILE)
        matches = rules.match('test_file.txt')  # Use the test file
        if matches:
            send_alert("Malware Detection Alert", f"Malware detected: {matches}")
        else:
            print("No malware detected.")
    except Exception as e:
        print(f"Failed to scan for malware: {e}")

def check_root_access():
    root_files = ['/system/app/Superuser.apk', '/sbin/su', '/system/bin/su', '/system/xbin/su', '/data/local/xbin/su', '/data/local/bin/su']
    for file in root_files:
        if os.path.exists(file):
            send_alert("Root Access Detected", "The system appears to be rooted.")
            return True
    return False

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(logged_in_as=request.get_json()), 200

if __name__ == "__main__":
    print("Starting system monitor...")
    logging.info("Starting system monitor...")
    if not check_root_access():
        check_disk_space()
        check_cpu_usage()
        sample_data = [[1], [2], [1], [2], [1], [2], [1], [2], [100]]  # Example data
        detect_fraud(sample_data)
        scan_for_malware()
    app.run(debug=True)
