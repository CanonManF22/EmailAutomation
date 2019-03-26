MY_ADDRESS = 
PASSWORD = 

def get_contacts(names, emails):
    # import name, email
    with open(names, 'r') as artist_names:
        with open (emails, 'r') as contact_emails:
            names = []
            emails = []
            for name in artist_names:
                #uppercase name
                uppercase_name = ''
                caps = name.split()
                for i, term in enumerate(caps):
                    if i == len(caps) - 1:
                        uppercase_name += term[0].upper() + term[1:]
                    else:
                        uppercase_name += term[0].upper() + term[1:] + ' '
                
                names.append(uppercase_name.replace('\n', ''))
            for contact in contact_emails:
                asset = contact.replace(' ', '')
                asset = asset.strip('\n')
                emails.append(asset.split(','))

    # for i in range(len(emails)):
    #     print(names[i], emails[i])
    return names, emails

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

names, emails = get_contacts('chella_2_names.txt', 'chella_2_emails.txt')

#SETUP SMTP SERVER
import smtplib

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

#SEND EMAILS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from string import Template

#TODO: remove test name and email
#print(emails)
#names = ['Avi Banerjee', 'John Doe']
#emails = [['avibanerjeephoto@gmail.com', 'avi.banerjee164@gmail.com'], ['avinash.banerjee@sjsu.edu', 'tman_avi@yahoo.com', 'sina.thousand@gmail.com']]
message_template = read_template('message1.txt')
for name, email in zip(names[45:], emails[45:]):
    print(name, email)
    msg = MIMEMultipart()       # create a message

    fromaddr = MY_ADDRESS
    toaddr = email[0]
    bcc = email[1:] if len(email) > 1 else []
    message_subject = "Coachella 2019: " + name + ' photographer'
    # add in the actual person name to the message template
    message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddr + "Subject: %s\r\n" % message_subject + "\r\n" + message_template.substitute(ARTIST_NAME=name.title())

    # setup the parameters of the message
    #AVI
    #msg['From']= 'Avi Banerjee'
    #sina
    msg['From']= 'Sina Mehran'
    msg['To']=email[0]
    #Avi
    # msg['Subject']= "Coachella 2019: " + name + ' photographer'
    msg['Subject']= name + " Coachella 2019 photographer"
    
    toaddrs = [toaddr] + bcc
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    msg = msg.as_string()
    # send the message via the server set up earlier.
    s.sendmail(MY_ADDRESS, toaddrs, message)
    
    del msg
    