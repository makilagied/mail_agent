# import smtplib
# from email.mime.text import MIMEText


# def send_email(to_email, subject, body):
#     sender_email = ""
#     sender_password = ""

#     message = MIMEText(body)
#     message["Subject"] = subject
#     message["From"] = sender_email
#     message["To"] = to_email

#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, to_email, message.as_string())





# import smtplib
# from email.mime.text import MIMEText
# import time

# from db_conn import fetch_clients

# def send_email(to_email, subject, body):
#     smtp_server = ""  
#     smtp_port = 25  
#     sender_email = ""
#     sender_password = ""  

#     message = MIMEText(body)
#     message["Subject"] = subject
#     message["From"] = sender_email
#     message["To"] = to_email

#     try:
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             # server.login(sender_email, sender_password)
#             server.sendmail(sender_email, to_email, message.as_string())
#             print(f"Email sent to {to_email}")
#     except Exception as e:
#         print(f"Failed to send email to {to_email}: {e}")

# def send_custom_emails(message_template):
#     clients = fetch_clients()
#     for name, email in clients:
#         customized_message = message_template.format(name=name)
#         send_email(email, "Customized Email", customized_message)
#         time.sleep(60)  # Throttle to 1 email per minute to avoid rate limits

# message_template = "Dear {name}, this is your customized message."
# send_custom_emails(message_template)
