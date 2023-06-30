import sys
from PyQt5 import uic
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtGui import*
import RPi.GPIO as GPIO
import time

led_pin = 15
buz_pin = 6
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, False)
GPIO.setup(buz_pin, GPIO.OUT)
pwm = GPIO.PWM(buz_pin, 1.0)


class qtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Day05/test1.ui',self)
        self.setWindowTitle('button')

        self.led_on.clicked.connect(self.led)
        self.led_off.clicked.connect(self.led)
        self.buz_on.clicked.connect(self.buz)
        self.buz_off.clicked.connect(self.buz)
        # self.buz_slider.valueChanged.connect(self.buz_s)
        # self.buz_slider.setMinimum(10)
        # self.buz_slider.setMaximum(30)
        # self.buz_slider.setTickInterval(5)


        self.btnEnd.clicked.connect(self.func_end)

    def led(self):
        name = self.sender().objectName()

        if name == 'led_on':
            GPIO.output(led_pin, True)
        if name == 'led_off':
            GPIO.output(led_pin, False)

    def buz(self):
        name = self.sender().objectName()

        if name == 'buz_on':
            pwm.start(1.0)
            pwm.ChangeFrequency(10.0)
            time.sleep(1)
        if name == 'buz_off':
            pwm.stop()

    # def buz_s(self):
    #     name = self.sender().objectName()

    #     if name == 'buz_slider':
    #         value=self.buz_slider.value()
    #         pwm.start(1.0)
    
    def func_end(self):
        name = self.sender().objectName()

        if name == 'btnEnd':
            GPIO.output(led_pin, False)
            pwm.stop()
    

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())