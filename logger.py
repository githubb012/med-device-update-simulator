from datetime import datetime

def log_event(message):
    """
    Records important application events to a log file.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/events.log", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")