import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html =Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Yiğit Özay'
email['to'] = 'example@gmail.com'
email['subject'] = ' example subject'

email.set_content(html.substitute(name ='oneone'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yourgmail@gmail.com', 'passwordofthegmail')
    smtp.send_message(email)
    