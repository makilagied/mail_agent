import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import logging

# Configure logging
logging.basicConfig(filename='email_logs.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(to_email, subject, body, attachments=None):
    smtp_server = ""
    smtp_port = 25
    sender_email = ""
    sender_password = ""  # Update if authentication is needed

    # Create a MIME message
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = to_email

    # Attach the body
    message.attach(MIMEText(body, "plain"))

    # Attach files
    if attachments:
        for attachment in attachments:
            try:
                attachment.seek(0)  # Ensure we're reading from the beginning of the file
                filename = os.path.basename(attachment.name)
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )
                message.attach(part)
            except Exception as e:
                logging.error(f"Failed to attach file {attachment.name}: {e}")
                print(f"Failed to attach file {attachment.name}: {e}")
                return False

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # server.login(sender_email, sender_password)  # Uncomment if authentication is required
            server.sendmail(sender_email, to_email, message.as_string())
            logging.info(f"Email sent to {to_email}")
            print(f"Email sent to {to_email}")
            return True
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")
        print(f"Failed to send email to {to_email}: {e}")
        return False
