import os
import subprocess

# Paths to the YARA executable, rule file, and directory to scan
yara_executable = r"C:\ProgramData\chocolatey\lib\yara\tools\yara64.exe"
rule_file = r"C:\Users\bhc11\Worm-detector\example_rule.yar"
directory_to_scan = r"C:\Users\bhc11\Documents"

# Command to run YARA scan
command = [yara_executable, "-r", rule_file, directory_to_scan]

# Run the command and capture the output
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print(result.stdout)
