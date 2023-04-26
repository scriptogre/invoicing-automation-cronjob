import smtplib
from email.message import EmailMessage
from config import OUTLOOK_EMAIL, OUTLOOK_PASSWORD, MAILHOG_HOST, MAILHOG_PORT, OUTLOOK_HOST, OUTLOOK_PORT
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader("templates"))


def send_outlook_email(email_subject: str, email_body: str, to_emails: str):
    msg = EmailMessage()
    msg.set_content(email_body, subtype="html")
    msg['Subject'] = email_subject
    msg['From'] = OUTLOOK_EMAIL
    msg['To'] = ', '.join(to_emails)

    if MAILHOG_HOST and MAILHOG_PORT:
        # MailHog is running, use SMTP
        with smtplib.SMTP(MAILHOG_HOST, MAILHOG_PORT) as server:
            server.send_message(msg)
    else:
        with smtplib.SMTP_SSL(OUTLOOK_HOST, OUTLOOK_PORT) as server:
            server.login(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)
            server.send_message(msg)
