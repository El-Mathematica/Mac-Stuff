import smtplib
import imapclient
import pyzmail
import ssl
import pprint





def usingimap():
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    password = input('Enter your password gokul')
    imapObj.login('programmerverbatim@gmail.com', password)
    pprint.pprint(imapObj.list_folders())
    imapObj.select_folder('[Gmail]/All Mail', readonly=True)
    UIDs = imapObj.search(['SINCE', '01-Feb-2019'])
    messages = imapObj.fetch(UIDs, ['BODY[]']) #Fetching Messages from UIDs
    # pprint.pprint(messages) #printing all messages
    formattedmessage = pyzmail.PyzMessage.factory(messages[9][b'BODY[]'])
    print(formattedmessage.get_subject()) #printing out the message using pyzmail


    



#starts smtp connection

def sendingmail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()

    password = input("Enter your password gokul")
    print(smtpObj.login('programmerverbatim@gmail.com', password))
    print(smtpObj.sendmail('programmerverbatim@gmail.com', 'menongokuls@gmail.com', 'Subject: Test\n This is a test'))

    smtpObj.quit()


usingimap()
