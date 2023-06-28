import RPi.GPIO as GPIO
import time

swPin = 14
ledPin = 15
buzPin = 6
cnt=1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(swPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzPin, GPIO.OUT)

GPIO.output(ledPin, False)
pwm = GPIO.PWM(buzPin, 1.0)	# 초기주파수 설정

def handler(channel):
	print("interrupt!")
	global cnt
	cnt +=1

GPIO.add_event_detect(swPin, GPIO.RISING, callback=handler)

try:
	while True:
		if cnt%2==1:
			GPIO.output(ledPin, True)
			pwm.start(1.0)
			pwm.ChangeFrequency(294)
			time.sleep(0.5)
			pwm.ChangeFrequency(523)
			time.sleep(0.5)
			for i in range(1,100):
				pwm.ChangeFrequency(i)
				time.sleep(0.2)
			pwm.stop()
		else:
			
			GPIO.output(ledPin, False)
			time.sleep(1.0)
			
		print(cnt%2)
			
except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
