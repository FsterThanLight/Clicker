import sys

from 窗体.test import Ui_test
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Test(QWidget, Ui_test):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer()
        self.pushButton.clicked.connect(self.start_Timer)
        self.pushButton_2.clicked.connect(self.end_Timer)
        self.pushButton_3.clicked.connect(self.break_time)
        self.timer.timeout.connect(self.showTime)
        self.lcdnumber = 0
        self.state = True

    def show_time(self):
        self.lcdNumber.display(self.lcdnumber)
        self.lcdnumber += 1

    def start_Timer(self):
        self.timer.start(1000)

    def end_Timer(self):
        self.lcdnumber = 0
        self.timer.stop()
        self.lcdNumber.display(self.lcdnumber)

    def break_time(self):
        if self.state:
            self.timer.stop()
            self.state = False
        else:
            self.timer.start(1000)
            self.state = True


if __name__ == "__main__":
    app = QApplication([])
    test = Test()
    test.show()
    sys.exit(app.exec_())
