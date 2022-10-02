"""
nel caso in cui venga lanciato un errore sul certificato ssl eseguire i seguenti passaggi:
- installare certifi
- eseguire lo script install_certifi.py
"""

from email.message import EmailMessage
import ssl
import smtplib
import csv

# credenziali di chi invia la mail
sender_mail = ""
password = ""

# oggetto e corpo della mai
subject = ""
body = ""


context = ssl.create_default_context()
with open("test-email.csv") as file:
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