"""
nel caso in cui venga lanciato un errore sul certificato ssl eseguire i seguenti passaggi:
- installare certifi
- eseguire lo script install_certifi.py
"""
from dotenv import load_dotenv
from email.message import EmailMessage
import os
import ssl
import smtplib
import csv

load_dotenv()
# credenziali di chi invia la mail
sender_mail = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

# oggetto e corpo della mai
subject = "formazione python"
body = "grazie per aver seguito la formazione"

context = ssl.create_default_context()
with open('test-email.csv') as file:
    reader = csv.reader(file)
    next(reader)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_mail, password)
        for email in reader:
            em = EmailMessage()
            em['From'] = sender_mail
            em['Subject'] = subject
            em.set_content(body)
            em['To'] = email
            smtp.sendmail(sender_mail, email, em.as_string())
            print(f"sent mail to {email}")
print("program finished")