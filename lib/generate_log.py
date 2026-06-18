
from datetime import datetime
import os

def generate_log(log_data):
    # STEP 1: Validate input
    # Check if data is a list; if not, raise a ValueError as required by the tests.
    if not isinstance(log_data, list):
        raise ValueError("Input data must be a list.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using file I/O
    # Use a with open() block and write each line from the data list
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
    
    # Return the filename so the Pytest fixtures can track and clean it up
    return filename