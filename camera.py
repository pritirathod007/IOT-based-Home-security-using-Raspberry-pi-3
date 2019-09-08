import picamera 
import time
camera=picamera.PiCamera()
camera.vflip = True
camera.resolution = (1024,768)
camera.capture=('example.jpg')
