

# Mail Agent

## Overview

**Mail Agent** is a Flask-based web application designed to send customized emails to multiple clients. The app allows users to specify an email heading, message template, and attach files that will be sent to each client. The emails are personalized with the client's name and can include multiple attachments.

## Features

- **Custom Email Heading and Message**: Specify the email's subject line and message template. Each email is personalized with the recipient's name.
- **File Attachments**: Attach multiple files that will be sent along with the emails.
- **Logging**: Logs the status of each email sent, including successes and errors.
- **Responsive Design**: The web interface is built with Bootstrap, ensuring that it is responsive and user-friendly on various devices.

## Technologies Used

- **Python 3.x**: The core programming language used for backend development.
- **Flask**: A micro web framework used to build the web application.
- **Bootstrap**: Used for creating a responsive and attractive web interface.
- **SMTP**: For sending emails.

## Prerequisites

- **Python 3.x**
- **Flask**
- **smtplib** (comes with Python standard library)
- **Bootstrap** (linked via CDN in the HTML)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <https://github.com/makilagied/mail_agent>
```

```bash
cd mail_agent
```

### 2. Install Dependencies

You need to install Flask as it’s the main dependency:

```bash
pip install flask
```

### 3. Configure SMTP Server

Edit the `send_email` function in `mail_server.py` to update the `sender_email` and `smtp_server` with your actual email address and SMTP server details. If authentication is required, uncomment and update the `sender_password`.

### 4. Run the Application

To start the Flask application on your machine's IP address:

```bash
python app.py
```

This will run the server on `http://0.0.0.0:5000`, making it accessible on the local network.

### 5. Access the Application

Open a web browser and navigate to:

```
http://<your-machine-ip>:5000
```

### 6. Sending Emails

- Fill in the email heading and message template.
- Attach files if needed.
- Click the "Send Emails" button.
- The application will display success and error messages based on the email-sending process.

## Logging

The application logs the status of each email sent, including the recipient's name, email, and whether the email was successfully sent or if there was an error.

## Dependencies

The project has a few dependencies that need to be installed:

1. **Flask**: The web framework used to build the application.
   
   Install via pip:
   
   ```bash
   pip install flask
   ```

2. **smtplib**: Used for sending emails via SMTP. This is part of Python’s standard library and does not need to be installed separately.

## Notes

- Create an additional folder called `attachments` in the project folder or change the directory in the `app.py` where all attachments will be uploaded before sending emails.
- Ensure that your SMTP server is properly configured and accessible from the machine running this application.
- The application throttles email sending to one email per second to avoid overwhelming the SMTP server.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue on the repository.


