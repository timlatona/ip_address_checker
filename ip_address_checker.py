import ipgetter
import credentials
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")

#import email
#from email.mime.text import MIMEtext

## information from credentials.py
gmail_email_from = credentials.login['send_from_email']
gmail_password = credentials.login['password']
gmail_email_to = credentials.login['send_to_email']
filepath = credentials.path
###

IP = ipgetter.myip()

f = open(filepath,"r")
fc = f.read()
if IP == fc:
    print(IP,fc)
    exit
else:
    print("difference noted")
    text = "Old IP was "+fc+"\n\nNew IP is: "+IP
    send_email(gmail_email_from,gmail_password,gmail_email_to,'IP Address change detected', text)
    f = open(filepath,"w")
    print(fc)
    print(IP)
    f.write(IP)
    f.close()


