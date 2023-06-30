import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('PyQt5 Example')
    
    label = QLabel('Hello, PyQt5!', window)
    label.move(20, 20)
    
    window.resize(250, 150)
    window.show()


    sys.exit(app.exec_())
