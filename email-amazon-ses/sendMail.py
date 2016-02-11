import sys
import os.path
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

#The security credentials of Amazon AWS. 
aws_access_key_id = "Your AWS Access Key ID"
aws_secret_access_key = "Your AWS Secret"

msg = MIMEText(sys.argv[2])
msg['Subject'] = sys.argv[1]
msg['From'] = sys.argv[3]
msg['To'] = sys.argv[4]

session = smtplib.SMTP("email-smtp.us-east-1.amazonaws.com",587)
session.ehlo()
session.starttls()
session.ehlo
session.login(aws_access_key_id, aws_secret_access_key)
session.sendmail(sys.argv[3], sys.argv[4].split(","), msg.as_string())
session.quit()
