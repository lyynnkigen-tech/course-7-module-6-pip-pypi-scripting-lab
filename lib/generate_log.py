from datetime import datetime
import os

def generate_log(data):
    # Requirement 3: The function raises a ValueError when called with invalid input (non-list types).
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    # Requirement 1 & 2: The filename follows the pattern log_YYYYMMDD.txt.
    # The generate_log() function creates a file with the correct timestamped filename.
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Requirement 4: File contents exactly match the input list
    # An empty list still creates a valid (empty) log file without errors.
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Requirement 5: The function prints a confirmation message including the filename.
    print(f"Log written to {filename}")

if __name__ == "__main__":
    # You can test it here if you like
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)