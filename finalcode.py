from picamera import PiCamera
import picamera
from time import sleep
import smtplib
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import RPiO.GPIO as GPIO 
import time
toaddr="your email id"
me="your email id"
my_password="your password"
Subject='alert'
GPIO.setmode(GPIO.BCM)
P=PiCamera()
P.resolution= (1024,768)
P.start preview()

GPIO.setup(11, GPIO.IN )
while True:
if GPIO.input(11):
    print("Motion...")
    time.sleep(2)
    P.capture( 'movement.jpg' )
    time.sleep(10)
    subject= ' Security alert!! '
    msg = MIMEMultipart()
    msg[ 'SUBJECT' ] = subject
    msg[ 'FROM' ] = me
    msg[ 'TO' ] = toaddr 
   
    fp = open( 'movement.jpg',  'rb')
    img = MIMEImage( fpread())
    fp.close()
    msg.attach(img)
   s=smtplib.SMPT_SSL( 'smtp.gmail.com')
    s.login(me, my_password)
    s.sendmail(me, toaddr, msg.as_string())
    print s
    s.quit()
