import RPi.GPIO as GPIO
import time

swPin = 14
ledPin = 15
cnt=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

def handler(channel):
	print("interrupt!")

GPIO.add_event_detect(swPin, GPIO.RISING, callback=handler)

try:
	while True:
		value = GPIO.input(swPin)
		
		if value==True:
			cnt+=1
			if cnt%2==1:
				GPIO.output(ledPin, True)
			GPIO.output(ledPin, False)
		
except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
