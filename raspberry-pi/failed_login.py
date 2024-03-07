import os
import re
from twilio.rest import Client

# twilio credentials and phone number
accounrd_sid = "[Redacted]"
auth_token = "[Redacted]"
twilio_phone_number = "[Redacted]"
recipient_phone_number = "[Redacted]"

last position = 0

# to check auth.log for new failed password attempts
def check_auth_log():
    global last_position
    try:
        with open('/var/log/auth.log', 'r') as auth_log:
            auth_log.seek(last_position)
            auth_log_content = auth_log.read()
            # Regular expression to extract date, time, IP address, port, and username
            log_pattern = r'(\w+ \d+ \d+:\d+:\d+) .* Failed password for (\w+) from (\d+\.\d+\.\d+\.\d+) port (\d+)'
            failed_attempts = re.findall(log_pattern, auth_log_content)
            if failed_attempts:
                last_position = auth_log.tell()  # Update the last processed log position
                return failed_attempts[-1]  # Return the last log details from new logs
    except FileNotFoundError:
        print("auth.log file not found.")
    return None

# to send Twilio notification
def send_twilio_notification(log_details):
    client = Client(account_sid, auth_token)
    date_time, username, ip_address, port = log_details
    message = f"Failed password attempt detected from User: {username}, IP Address: {ip_address}, Port: {port}, Date/Time: {date_time}"
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

# daemon function
def run_daemon():
    while True:
        failed_attempt = check_auth_log()
        if failed_attempt:
            send_twilio_notification(failed_attempt)
            print("Notification sent.")
        time.sleep(60)  # Check the log file every 60 seconds

# main function
if __name__ == "__main__":
    with daemon.DaemonContext():
        run_daemon()
