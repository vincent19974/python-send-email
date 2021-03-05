import smtplib, ssl
import getpass
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "nambatac.vince@gmail.com"  # Enter your address
receiver_email = "vincent@apolloglobal.net"  # Enter receiver address
password = getpass.getpass("Type your password and press enter: ")
message = """\
Subject: Your PC is about to shutdown

This message was sent to you to let you know that there is someone attempted to shutdown your PC."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
