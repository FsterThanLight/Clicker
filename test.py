import sys

from 窗体.test import Ui_test
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Test(QWidget, Ui_test):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__=="__main__":
    app=QApplication([])
    test=Test()
    test.show()
    sys.exit(app.exec_())