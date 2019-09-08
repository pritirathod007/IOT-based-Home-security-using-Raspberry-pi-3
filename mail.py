import time
from datetime import datetime
import picamera
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
with picamera.PiCamera() as camera
camera.resolution = (1024,768)
camera.vflip = True
camera.start_preview()
#Camera warm up time
time.sleep(2)
camera.capture('photo.jpg')
f_time=datetime.now().strftime('%a %d %b @ %H:%M')
you = 'email id'
me = 'email id'
my_password = ' '
subject = 'Photo' + f_time
msg = MIMEMultipart()
msg[ 'SUBJECT' ] = subject
msg[ 'FROM' ] = me
msg[ 'TO' ] = you
msg.preamble = " Photo @ " + f_time
fp = open( 'photo.jpg',  'rb')
img = MIMEImage( fpread())
fp.close()
msg.attach(img)
s=smtplib.SMPT_SSL( 'smtp.gmail.com')
s.login(me, my_password)
s.sendmail(me, you, msg.as_string())
print s
s.quit()
