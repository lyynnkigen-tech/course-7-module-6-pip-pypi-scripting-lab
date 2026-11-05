
"""Write a list of log entries to a timestamped text file."""

from datetime import datetime


def generate_log(data):
    """Write each entry in ``data`` to ``log_YYYYMMDD.txt``.

    Args:
        data (list): Log entries to write, one per line.

    Returns:
        str: The name of the file that was created.

    Raises:
        ValueError: If ``data`` is not a list.
    """
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)