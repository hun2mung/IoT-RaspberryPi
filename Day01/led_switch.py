import RPi.GPIO as GPIO
import time

btn = 14
led = 15
cnt = 0

def handler(channel):   # 버튼 클릭을 인지하려 cnt 변수를 가진 함수
    global cnt
    cnt = cnt+1
    print(cnt)

GPIO.setwarnings(False) # 필요없는 warning문구 해결
GPIO.setmode(GPIO.BCM)  # BCM / BOARD

GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  # 버튼을 눌렀을때 GPIO.IN으로 버튼 눌리는거 인식
GPIO.add_event_detect(btn, GPIO.RISING, callback=handler)
GPIO.setup(led, GPIO.OUT)

while True:
    if(cnt%2==1):
        GPIO.output(led, True)
    GPIO.output(led, False)

GPIO.cleanup()