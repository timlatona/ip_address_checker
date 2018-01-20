import ipgetter
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

IP = ipgetter.myip()
f = open("c:\\\\\\Users\\\Timnew\\\Documents\\\Python\\\Docs\\\ip.txt","r")
fc = f.read()
if IP == fc:
    print(IP,fc)
    exit
else:
    print("difference noted")
    text = "Old IP was "+fc+"\n\nNew IP is: "+IP
    send_email('latonapython@gmail.com','Sumo21Lima','latona@gmail.com','IP Address change detected', text)
    f = open("c:\\\\\\Users\\\Timnew\\\Documents\\\Python\\\Docs\\\ip.txt","w")
    print(fc)
    print(IP)
    f.write(IP)
    f.close()


