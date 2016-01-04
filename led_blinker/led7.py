import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
x=0.2

while True:
	GPIO.output(11, True)
	time.sleep(0.5)
	GPIO.output(11, False)
	time.sleep(0.5)
