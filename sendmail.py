# --------------------------------------------------------------------------
# import yagmail
# yagmail.register('SenderMail@gmail.com', '16 Character Password')
# --------------------------------------------------------------------------

import yagmail
import os

receiver = "deepakraj33333@gmail.com"
body = "Attendence File"
filename = "Attendance"+os.sep+"Attendance.csv" 

yag = yagmail.SMTP('seema.dubai.nepal@gmail.com')

try:
    yag.send(
    to=receiver,
    subject="Attendance Report",
    contents=body, 
    attachments=filename)
    print("Email sent successfully!")

except Exception as e:
    print("Failed to send email: {e}")