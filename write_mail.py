import smtplib
from email.message import EmailMessage

def send_mail(name,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('#your email id','#your password')
    email = EmailMessage()
    email['From'] = '#your email id'
    email['To'] = name
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

mail_id = {
                '#contact' : '#contact@gmail.com',
                '#contact_1' : 'contact_1@gmail.com',
                'contact_2' : 'contact_2@gmail.com'
        }

name = input('Which one you want to send : ')
subject = input('Enter the subject : ')
content = input('Enter the message : ')
send_mail(mail_id[name],subject,content)
