import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

import RPi.GPIO as GPIO
import time

class qtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./test.ui',self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())
    