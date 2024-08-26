from db_conn import fetch_clients
from mail_server import send_email
import time

def send_custom_emails(heading, message_template):
    clients = fetch_clients()
    for name, email in clients:
        salutations = "Dear {name},"
        customized_message = message_template.format(name=name)
        full_message = f"{salutations}\n\n{customized_message}"
        send_email(email, heading, full_message)
        print(f"Email sent to {name} at {email}")
        time.sleep(1)  # Throttle to 1 email per sec to avoid rate limits

if __name__ == "__main__":
    # This can be triggered through the web interface, not directly here
    pass
