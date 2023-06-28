import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

segments = [17,27,22,10,9,11,5]
btn = 14
cnt = 0

def handler(channel):
	global cnt
	cnt += 1
	print(cnt)

digits = ((1,1,1,1,1,1,0),
				  (0,1,1,0,0,0,0),
				  (1,1,0,1,1,0,1),
				  (1,1,1,1,0,0,1),
				  (0,1,1,0,0,1,1),
				  (1,0,1,1,0,1,1),
				  (1,0,1,1,1,1,1),
				  (1,1,1,0,0,0,0),
				  (1,1,1,1,1,1,1),
				  (1,1,1,1,0,1,1))

GPIO.setup(segments[0], GPIO.OUT)
GPIO.setup(segments[1], GPIO.OUT)
GPIO.setup(segments[2], GPIO.OUT)
GPIO.setup(segments[3], GPIO.OUT)
GPIO.setup(segments[4], GPIO.OUT)
GPIO.setup(segments[5], GPIO.OUT)
GPIO.setup(segments[6], GPIO.OUT)

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn, GPIO.RISING, callback=handler)

while(True):
		i = cnt%9
		GPIO.output(segments[0], digits[i][0])
		GPIO.output(segments[1], digits[i][1])
		GPIO.output(segments[2], digits[i][2])
		GPIO.output(segments[3], digits[i][3])
		GPIO.output(segments[4], digits[i][4])
		GPIO.output(segments[5], digits[i][5])
		GPIO.output(segments[6], digits[i][6])
		time.sleep(1)
GPIO.cleanup()
