import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def text_content(sender: str, fname: str, lname: str, message: str) -> str:
    text = f"email: {sender}\nname: {fname} {lname}\nmessage: {message}"
    return text

def send_email(smtp_server, port, login, password, to_email, text):
    try:
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart()
        msg['Subject'] = "Contact Form Response"
        msg['From'] = login
        msg['To'] = to_email

        # Record the MIME type of the text part - text/plain.
        part1 = MIMEText(text, 'plain')

        # Attach part into message container.
        msg.attach(part1)

        print("Connecting to SMTP server...")
        # Send the message via local SMTP server.
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.ehlo()  
            # print("Logging in to SMTP server...")
            server.login(login, password)
            # print("Sending email...")
            server.sendmail(login, to_email, msg.as_string())
            server.quit()  
        # print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError as e:
        print("Failed to authenticate with the SMTP server. Check your login credentials.")
        print(f"Error: {e}")
    except smtplib.SMTPConnectError as e:
        print("Failed to connect to the SMTP server. Check the SMTP server address and port.")
        print(f"Error: {e}")
    except smtplib.SMTPException as e:
        print("Failed to send email. SMTP error occurred.")
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")




