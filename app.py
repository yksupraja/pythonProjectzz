import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request

app = Flask(__name__)

def send_email(name, email, message):
    # Email configuration
    email_server = 'smtp.gmail.com'  # Replace with your email server
    email_port = 465
    email_username = 'supraja2d@gmail.com'  # Replace with your email address
    email_password = 'pndsmcfwifbnbhyv'  # Replace with your email password

    # Create an SMTP instance
    smtp_server = smtplib.SMTP_SSL(email_server, email_port)

    # Log in to the server
    smtp_server.login(email_username, email_password)

    # Create an email message
    subject = 'New Message from Contact Form'
    body = f"Name: {name}\nEmail: {email}\n\n{message}"

    message = MIMEMultipart()
    message['From'] = email_username
    message['To'] = 'supraja.21iamos126@iadc.ac.in'  # Replace with recipient email address
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Send the email
    smtp_server.sendmail(email_username, 'supraja.21iamos126@iadc.ac.in', message.as_string())

    # Quit the SMTP server
    smtp_server.quit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email_route():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    send_email(name, email, message)

    return "Email sent successfully"

if __name__ == '__main__':
    app.run()
