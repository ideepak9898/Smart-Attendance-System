# --------------------------------------------------------------------------
# import yagmail
# yagmail.register('SenderMail@gmail.com', '16 Character Password')

# To get 16 Character Password follow this link 'https://docs.google.com/document/d/1i0tNNIsRysp_Z8BfgwyIJK-B2A1fikgnHYgatECI6jA/edit?usp=sharing'
# --------------------------------------------------------------------------

import yagmail
import os

receiver = "ReceiverMail@gmail.com"
body = "Attendence File"
filename = "Attendance"+os.sep+"Attendance.csv" 

yag = yagmail.SMTP('SenderMail@gmail.com')

try:
    yag.send(
    to=receiver,
    subject="Attendance Report",
    contents=body, 
    attachments=filename)
    print("Email sent successfully!")

except Exception as e:
    print("Failed to send email: {e}")
