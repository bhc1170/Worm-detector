
import logging

logging.basicConfig(filename='worm_detector.log', level=logging.INFO)

def log_detection(file_path):
    logging.info(f"Suspicious file detected: {file_path}")

# Usage example
if __name__ == "__main__":
    log_detection('/path/to/suspicious/file')
