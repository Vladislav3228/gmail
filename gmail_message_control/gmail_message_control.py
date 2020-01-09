import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
retcode, capabilities = mail.login('что-то тут@gmail.com', 'какой-то пароль')
mail.select('INBOX')
n = 0
retcode, messages = mail.search(None, '(UNSEEN)')
if retcode == 'OK':
   for num in messages[0].split() :
      print ('Processing ')
      n=n+1
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_bytes(response_part[1])
             raw_email = data[0][1]
             raw_email_string = raw_email.decode('utf-8')
             email_message = email.message_from_string(raw_email_string)
             for part in email_message.walk():
                        if (part.get_content_type() == "text/plain" or part.get_content_type() == "image/jpeg"): # ignore attachments/html
                              body = part.get_payload(decode=True)                          
                              print(original['From'])
                              print(original['From'])
                              print(original['Subject'])            
                              print(body.decode('utf-8'))
                              print('**********\n')
                              
                        else:
                              continue
             typ, data = mail.store(num,'+FLAGS','\\Seen')
mail.close()
mail.logout()