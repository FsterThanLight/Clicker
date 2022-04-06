import pyautogui
import pyperclip
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from 窗体.add_instruction import Ui_Dialog
from 窗体.mainwindow import Ui_MainWindow
import sys


class Main_window(QMainWindow, Ui_MainWindow):
    """继承窗体的类，实现窗体和逻辑代码分离"""

    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    main_window = Main_window()
    # 给窗体程序设置图标
    main_window.setWindowIcon(QIcon('图标.ico'))
    # 显示窗体
    main_window.show()
    sys.exit(app.exec_())
