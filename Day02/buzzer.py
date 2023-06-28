import RPi.GPIO as GPIO
import time

pinbuz = 6	# 버즈핀번호

#도레미파솔라시도
melody = [261,294,329,349,392,440,493,523]

GPIO.setwarnings(False)	# 쓸모없는 warning 제거
GPIO.setmode(GPIO.BCM)	# BCM GPIO 모드
GPIO.setup(pinbuz, GPIO.OUT)	# 부저 세팅

pwm = GPIO.PWM(pinbuz, 1.0)	# 초기 주파수 설정 1.0Hz

try:
	while(True):
		key=int(input())-1
		if key >= 0 and key < len(melody):
			pwm.start(1.0)	# 부저 스타트
			pwm.ChangeFrequency(melody[key])
			time.sleep(0.5)
			pwm.stop()
		else:
			print("에러")
except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()


