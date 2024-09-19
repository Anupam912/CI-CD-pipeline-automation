# python/notify_failure.py
import smtplib
from email.mime.text import MIMEText

def send_failure_email():
    sender = 'your_email@example.com'
    receivers = ['team@example.com']
    
    msg = MIMEText("Deployment failed. Please check logs for more details.")
    msg['Subject'] = 'Deployment Failure Notification'
    msg['From'] = sender
    msg['To'] = ", ".join(receivers)

    with smtplib.SMTP('smtp.example.com') as smtp:
        smtp.sendmail(sender, receivers, msg.as_string())

if __name__ == "__main__":
    send_failure_email()
