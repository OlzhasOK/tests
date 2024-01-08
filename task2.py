import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

def send_email(file_path, recipient_email):
    sender_email ="oljabay1@gmail.com"
    sender_password = "xjni darq fkkc aens"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Файл из первого задания'

    body = 'Отправляю вам файл, который был сгенерирован кодом из 1 задания'
    msg.attach(MIMEText(body, 'plain'))

    with open(file_path, 'rb') as file:
        attachment = MIMEApplication(file.read(), Name=os.path.basename(file_path))
        attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        msg.attach(attachment)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

    print(f"Файл успешно отправлен на адрес {recipient_email}")

file_path_to_send = r"C:\Users\77083\Documents\skcu\Lindsay_2024-01-08_497.xlsx"
recipient_email_to_send =  "olzhas_kz_olzhabay@mail.ru"

send_email(file_path_to_send, recipient_email_to_send)
