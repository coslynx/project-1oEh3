```python
# logging.py

import datetime

def log_action(action, user_id, reason=None):
    timestamp = datetime.datetime.now()
    if reason:
        log_entry = f"{timestamp} - {action} by user {user_id} with reason: {reason}"
    else:
        log_entry = f"{timestamp} - {action} by user {user_id}"
    
    with open("moderation_log.txt", "a") as log_file:
        log_file.write(log_entry + "\n")

def retrieve_logs():
    try:
        with open("moderation_log.txt", "r") as log_file:
            logs = log_file.readlines()
        return logs
    except FileNotFoundError:
        return []

# Additional functions can be added as needed for more advanced logging features
```
This code provides functions to log moderation actions with timestamps and retrieve the log history. The log entries are saved in a file called "moderation_log.txt" for record-keeping purposes.