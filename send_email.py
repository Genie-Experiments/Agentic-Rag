import smtplib,ssl
from dotenv import load_dotenv
import os
from llama_index.core.tools import FunctionTool

load_dotenv()

def send_email(receiver_email, message):
    
    sender_email = os.getenv("SENDER_EMAIL_ADDRESS")
    sender_password = os.getenv("SENDER_EMAIL_APP_PASSWORD")

    host = "smtp.gmail.com"
    port = 587
    
    context = ssl.create_default_context()

    print("Sender email ",sender_email)
    print("Sender password ",sender_password)
    print("Receiver email ",receiver_email)

    with smtplib.SMTP(host,port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email,sender_password)
        server.sendmail(sender_email, receiver_email, message)

email_send_tool = FunctionTool.from_defaults(
    fn=send_email,
    name="send_email",
    description="""this tool sends an email to the mentioned email address. Use this when you need to send an email."""
)

if __name__ == "__main__":
    send_email("shazilahmed445@gmail.com","test email")