import requests
from smtplib import SMTP

# Define function to check website status
def check_website(website):
    try:
        response = requests.get(website.url)
        if response.status_code == 200:
            website.status = 'up'
        else:
            website.status = 'down'
    except:
        website.status = 'down'
    db.session.commit()
# Define function to send email
def send_email(smtp_server, sender_email, recipient_email, subject, body):
    message = f'Subject: {subject}\n\n{body}'
    with SMTP(smtp_server) as server:
        server.sendmail(sender_email, recipient_email, message)

