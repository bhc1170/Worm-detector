import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
import threading

# Function to simulate the scanning process
def start_scan():
    scan_button.config(state=tk.DISABLED)
    log_message("Starting scan...")

    # Simulate a scanning process
    for i in range(5):
        time.sleep(1)  # Simulating work with sleep
        progress_var.set((i + 1) * 20)
        root.update_idletasks()

    log_message("Scan completed.")
    messagebox.showinfo("Scan Status", "Scan completed successfully!")
    scan_button.config(state=tk.NORMAL)

# Function to add log messages
def log_message(message):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.config(state=tk.DISABLED)

# Function to run the scan in a separate thread
def start_scan_thread():
    threading.Thread(target=start_scan).start()

# Set up the main application window
root = tk.Tk()
root.title("Worm Detector")

# Create a label for the title
title_label = tk.Label(root, text="Worm Detector", font=("Arial", 16))
title_label.pack(pady=10)

# Create a progress bar
progress_var = tk.IntVar()
progress_bar = Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill=tk.X, padx=20, pady=10)

# Create a button to start the scan
scan_button = tk.Button(root, text="Start Scan", command=start_scan_thread)
scan_button.pack(pady=10)

# Create a text widget to display logs
log_text = tk.Text(root, state=tk.DISABLED, height=10)
log_text.pack(fill=tk.BOTH, padx=20, pady=10)

# Start the main application loop
root.mainloop()
