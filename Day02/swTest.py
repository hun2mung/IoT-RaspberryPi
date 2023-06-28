import RPi.GPIO as GPIO
import time

swPin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)

def handler(channel):
	print("interrupt!")

GPIO.add_event_detect(swPin, GPIO.RISING, callback=handler)

try:
	while True:
		pass 
except keyboardInterrupt:
	GPIO.cleanup()
