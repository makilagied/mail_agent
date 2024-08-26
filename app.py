from db_conn import fetch_clients
from flask import Flask, request, render_template, jsonify
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import logging

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'attachments/'

# Configure logging
logging.basicConfig(filename='email_logs.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(to_name, to_email, subject, body, attachments=None):
    smtp_server = " "
    smtp_port = 25
    sender_email = " "
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
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # server.login(sender_email, sender_password)  # Uncomment if authentication is required
            server.sendmail(sender_email, to_email, message.as_string())
            log_msg = f"Email sent to {to_name} .. {to_email}"
            logging.info(log_msg)
            print(log_msg)
            return log_msg
    except Exception as e:
        error_msg = f"Failed to send email to {to_name} .. {to_email} with error message: {e}"
        logging.error(error_msg)
        print(error_msg)
        return error_msg
    

def save_attachments(files):
    saved_files = []
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    for file in files:
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            try:
                file.save(file_path)
                saved_files.append(open(file_path, 'rb'))  # Open file for reading
            except Exception as e:
                print(f"Failed to save attachment {file.filename}: {e}")
                log_msg = f"Failed to save attachment {file.filename}: {e}"
                logging.error(log_msg)
    
    return saved_files

def send_custom_emails(heading, message_template, attachments):
    clients = fetch_clients()  # This should be your function to get clients
    successes = []
    errors = []
    for name, email in clients:
        salutation = f"Dear {name},"
        customized_message = message_template.format(name=name)
        full_message = f"{salutation}\n\n{customized_message}"
        result = send_email(name, email, heading, full_message, attachments)
        if "Failed" in result:
            errors.append(result)
        else:
            successes.append(result)
        time.sleep(1)  # Throttle to 1 email per sec
    
    return {"successes": successes, "errors": errors}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_emails', methods=['POST'])
def handle_send_emails():
    heading = request.form['heading']
    message_template = request.form['message']
    files = request.files.getlist('attachments')
    
    # Save and process attachments
    attachments = save_attachments(files)
    
    # Send emails and get results
    results = send_custom_emails(heading, message_template, attachments)
    
    # Close files
    for file in attachments:
        file.close()
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



