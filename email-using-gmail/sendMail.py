import sys
import os.path
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


email_id = "Your email ID"
email_password = "Your email password"

msg = MIMEText(sys.argv[2])
msg['Subject'] = sys.argv[1]
msg['From'] = sys.argv[3]
msg['To'] = sys.argv[4]

# Send the email via gmail SMTP server.
session = smtplib.SMTP("smtp.gmail.com",587)
session.ehlo()
session.starttls()
session.ehlo
session.login(email_id, email_password)
session.sendmail(sys.argv[3], sys.argv[4].split(","), msg.as_string())
session.quit()
