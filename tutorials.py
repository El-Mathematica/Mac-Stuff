import imapclient 
import thepassword


imapObject = imapclient.IMAPClient('imap.gmail.com', ssl=True)

imapObject.login("programmerverbatim@gmail.com", thepassword.passwords())

print(imapObject.list_folders())

imapObject.select_folder('INBOX', readonly = True)

print(imapObject.search(["SINCE", "01-Feb-2019"]))


                
