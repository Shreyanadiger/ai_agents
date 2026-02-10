import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrets import sender_email, receiver_email, password

def send_email(receiver_email: str, content: str) -> str:
    """Send an email to the given receiver_email with the given content."""
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "hello vaishnavi from shrey"
    body = content
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    send_email(receiver_email, "hello vaish have a good day.")