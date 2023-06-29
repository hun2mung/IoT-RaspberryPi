import RPi.GPIO as GPIO	# RPi.GPIO에 정의된 기능을 GPIO라는 명칭으로 사용
import time	# time 모듈

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)	# GPIO 이름 BCM 명칭 사용

trig_pin = 24	# trig핀 24번(송신)
echo_pin = 23	# echo핀 23번(수신)
buz_pin = 6	# buz핀 6번

GPIO.setup(trig_pin, GPIO.OUT)	# 초음파 신호 전송핀 출력지정
GPIO.setup(echo_pin, GPIO.OUT)	# 초음파 신호 수신핀 출력지정
GPIO.setup(buz_pin, GPIO.OUT)

GPIO.output(trig_pin, False)
pwm = GPIO.PWM(buz_pin, 1.0)	# 초기 주파수 1.0Hz
print("초음파 출력 초기화")

try:
	while 1:
		GPIO.output(trig_pin, True)
		time.sleep(0.00001)
		GPIO.output(trig_pin, False)

		while GPIO.input(echo_pin)==0:	# echo핀 OFF가 시작점
			start = time.time()
		while GPIO.input(echo_pin)==1:	# echo핀 ON이 되는 시점이 반사파 수신시간 
			stop = time.time()

		checktime = stop - start	# 초음파 송수신되는 시간
		dis = checktime * 34300/2
		print("DISTANCE : %.1f cm" % dis)
		time.sleep(0.2)
		
		if 4 <= dis and dis < 6 :
			pwm.start(50)	# 듀티비 50%
			pwm.ChangeFrequency(600)
			time.sleep(0.01)
			pwm.stop()
			time.sleep(0.01)
		elif 6 <= dis :
			pwm.start(50)
			pwm.ChangeFrequency(600)
			time.sleep(0.1)
			pwm.stop()
			time.sleep(0.1)
		else:
			pwm.stop()
			time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
