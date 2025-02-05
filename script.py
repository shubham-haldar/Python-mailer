import smtplib
from email.mime.text import MIMEText # MINEText is a class that part of the e mail
from email.mime.multipart import MIMEMultipart
import os

def send_mail(workflow_name, repo_name,workflow_run_id ):
    # Email details
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    # Email message
    subject = f"Workflow {workflow_name} failed for this repo {repo_name}"
    body = f"Hi, the workflow {workflow_name} failed gor this repo {repo_name} please check the logs for more details .\n More details:.\n: {workflow_run_id}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        print('Email sent successfully')
    except Exception as e:
        print(f'Error: {e}')


send_mail(os.getenv('WORKFLOW_NAME '), os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))