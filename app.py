from flask import Flask, request, render_template, jsonify
from mail_server import send_email
from db_conn import fetch_clients
import time
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'attachments/'

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
    
    return saved_files

def send_custom_emails(heading, message_template, attachments):
    clients = fetch_clients()
    results = []
    for name, email in clients:
        salutation = f"Dear {name},"
        customized_message = message_template.format(name=name)
        full_message = f"{salutation}\n\n{customized_message}"
        try:
            send_email(email, heading, full_message, attachments)
            results.append(f"Email sent to {name} at {email}")
        except Exception as e:
            results.append(f"Failed to send email to {name} at {email}: {e}")
        time.sleep(1)  # Throttle to 1 email per sec
    
    return results

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
    app.run(debug=True)
