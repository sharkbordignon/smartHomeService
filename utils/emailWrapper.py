import sys
sys.path.append('config')
import config as cfg

_login_ = cfg.email['email']
_password_ = cfg.email['key']

import smtplib

from  email.MIMEMultipart import MIMEMultipart
from  email.MIMEText import MIMEText

def sendEmail(to, result, datetime):
  server = __setupEmail()
  email = __createMessenge(to, result, datetime)
  server.sendmail(_login_, to, email)
  server.quit()

def __setupEmail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(_login_, _password_)
  return server

def __createMessenge(to, msgs, datetime):
  body = "Report #" + str(datetime) + "# \n"
  for i in msgs:
    body = body + i + "\n"
  msg = MIMEMultipart()
  msg['From'] = _login_
  msg['To'] = to
  msg['Subject'] = 'House report'
  msg.attach(MIMEText(body, 'plain'))
  email = msg.as_string()
  return email

#tests#
import datetime
sendEmail(_login_, 'my message,', str(datetime.datetime.now()))
