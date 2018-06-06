import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMail(sender, userPass, toaddr):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = toaddr
    msg['Subject'] = 'Automated message'

    body = "This is an automated test message to multiple parties"
    msg.attach(MIMEText(body, 'plain'))
    #what are these values below for optum's servers?
    server = smtplib.SMTP('casx10.uhc.com', 587)
    server.starttls()
    server.login(sender, userPass)
    text = msg.as_string()
    server.sendmail(sender, toaddr, text)
    server.quit()

sendees = ["devlin.brennan@example.com", "tien.bui@example.com"]
for sendee in sendees:
    sendMail("devlin.brennan@example.com", "", sendee)

