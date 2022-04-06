import pyautogui
import pyperclip
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget
from 窗体.add_instruction import Ui_Form
from 窗体.mainwindow import Ui_MainWindow
import sys


class Main_window(QMainWindow, Ui_MainWindow):
    '''主窗口'''
    def __init__(self,dialog_1):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)
        self.toolButton.clicked.connect(lambda: self.show_dialog(dialog_1))

    def show_dialog(self,dialog_1):
        dialog_1.show()

class Dialog(QWidget, Ui_Form):
    '''添加指令对话框'''
    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    dialog_1=Dialog()
    main_window = Main_window(dialog_1)
    # 给窗体程序设置图标
    main_window.setWindowIcon(QIcon('图标.ico'))
    # 显示窗体
    main_window.show()
    # 显示添加对话框窗口
    sys.exit(app.exec_())
