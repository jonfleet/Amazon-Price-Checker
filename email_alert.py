
import os
import config
import smtplib
from Network_programs import Soupbot

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_PASSWORD = 'Iliketocodealot112@'
EMAIL_ADDRESS = 'pybot1@outlook.com'

# with smtplib.SMTP_SSL('smtp-mail.outlook.com', 587) as smtp:
with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    
    price = Soupbot().findPrice()
    productTitle = Soupbot().findName()
    # print(price)
    # print(productTitle.len())    
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject = 'Price Tracker'
    body = "The program has finished running. The price of " + productTitle + " is currently " + price
    body = body.encode()
    msg = f'Subject:{subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS,['jmfleet1@gmail.com'],msg)
    print("Email Sent!")





# class EmailAlert(object):
#     """Class for sending email alert from slave account"""
#     def __init__(self, subject, msg):

#         self.subject = subject
#         self.msg = msg

#     def send_email(self):
#         # try:
#             server = smtplib.SMTP(host = 'smtp.mail.com', port ='587')
#             server.ehlo()
#             server.starttls()
#             server.login('pybot@mail.com', 'Ilikecode@174')
#             # server.login(config.FROM_EMAIL_ADDRESS, config.PASSWORD)
#             message = 'Subject: {}\n\n{}'.format(self.subject, self.msg)
#             server.sendmail('pybot@mail.com','jmfleet1@gmail.com',message)
#             # server.sendmail(config.FROM_EMAIL_ADDRESS,config.TO_EMAIL_ADDRESS,message)
#             server.quit()
#             print("Success: Email sent!")
#         # except:
#             # print("Email failed to send.")

# EmailAlert("Test","Hello from PY bot").send_email()