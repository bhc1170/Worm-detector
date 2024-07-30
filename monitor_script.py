import os
import time

# Directory to monitor
DIRECTORY_TO_WATCH = "."
# Threshold for alerting
ALERT_THRESHOLD = 10
# Time interval to check (in seconds)
CHECK_INTERVAL = 5

# Dictionary to keep track of file modifications
file_modifications = {}

def monitor_directory():
    """Monitors the directory for unusual file activities."""
    print(f"Monitoring directory: {DIRECTORY_TO_WATCH}")
    
    # Get the initial state of the directory
    initial_files = set(os.listdir(DIRECTORY_TO_WATCH))

    while True:
        time.sleep(CHECK_INTERVAL)
        current_files = set(os.listdir(DIRECTORY_TO_WATCH))

        # New files detection
        new_files = current_files - initial_files
        for file in new_files:
            print(f"New file detected: {file}")
            file_modifications[file] = file_modifications.get(file, 0) + 1

        # Modified files detection (simplified as re-detected files)
        for file in current_files & initial_files:
            file_path = os.path.join(DIRECTORY_TO_WATCH, file)
            if os.path.isfile(file_path):
                last_mod_time = os.path.getmtime(file_path)
                if file not in file_modifications:
                    file_modifications[file] = last_mod_time
                else:
                    if file_modifications[file] != last_mod_time:
                        print(f"File modified: {file}")
                        file_modifications[file] = last_mod_time

        # Check for alert condition
        if len(new_files) > ALERT_THRESHOLD:
            print(f"Alert: High file activity detected! {len(new_files)} new files detected.")
        
        # Update the set of files for the next iteration
        initial_files = current_files

if __name__ == "__main__":
    monitor_directory()
