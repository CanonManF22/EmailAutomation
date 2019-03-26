# MY_ADDRESS = 'avi.banerjee164@gmail.com'
# PASSWORD = 'PwrMvsOnly97'

# def get_contacts(names, emails):
#     # import name, email
#     with open(names, 'r') as artist_names:
#         with open (emails, 'r') as contact_emails:
#             names = []
#             emails = []
#             for name in artist_names:
#                 #uppercase name
#                 uppercase_name = ''
#                 caps = name.split()
#                 for i, term in enumerate(caps):
#                     if i == len(caps) - 1:
#                         uppercase_name += term[0].upper() + term[1:]
#                     else:
#                         uppercase_name += term[0].upper() + term[1:] + ' '
                
#                 names.append(uppercase_name.replace('\n', ''))
#             for contact in contact_emails:
#                 emails.append(contact.strip('\n'))
                
#     return names, emails

# from string import Template

# def read_template(filename):
#     with open(filename, 'r', encoding='utf-8') as template_file:
#         template_file_content = template_file.read()
#     return Template(template_file_content)

# names, emails = get_contacts('mycontacts1.txt', 'mycontacts2.txt')
# for i in range(len(names)):
#     print(i+2, names[i], emails[i])

# #SETUP SMTP SERVER
# import smtplib

# s = smtplib.SMTP(host='smtp.gmail.com', port=587)
# s.starttls()
# s.login(MY_ADDRESS, PASSWORD)

# #SEND EMAILS
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# print(emails[53:])
# TODO: remove test name and email
# names = ['Avi Banerjee', 'John Doe']
# emails = [['avibanerjeephoto@gmail.com', 'avi.banerjee164@gmail.com'], ['avinash.banerjee@sjsu.edu', 'tman_avi@yahoo.com']]
# message_template = read_template('message.txt')
# for name, email in zip(names[53:], emails[53:]):
#     print(name, email)
#     msg = MIMEMultipart()       # create a message

#     # add in the actual person name to the message template
#     message = message_template.substitute(ARTIST_NAME=name.title())

#     # setup the parameters of the message
#     msg['From']= 'Avi Banerjee'
#     msg['To']=",".join(email)
#     msg['Subject']= name + " Test Tracked Emails"

#     # add in the message body
#     msg.attach(MIMEText(message, 'plain'))
#     msg = msg.as_string()
#     # send the message via the server set up earlier.
#     #s.sendmail(MY_ADDRESS, email, msg)
    
#     del msg
    

