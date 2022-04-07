import pyautogui
import pyperclip
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidgetItem, QMessageBox
from 窗体.add_instruction import Ui_Form
from 窗体.mainwindow import Ui_MainWindow
import sys
import os


class Main_window(QMainWindow, Ui_MainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)
        # 实例化子窗口1
        self.dialog_1 = Dialog()
        self.tableWidget.setColumnWidth(4, 50)
        # 添加指令按钮
        self.toolButton.clicked.connect(self.show_dialog)
        # 获取数据，修改按钮
        self.toolButton_5.clicked.connect(self.get_data)
        # 获取数据，子窗体取消按钮
        self.dialog_1.pushButton_2.clicked.connect(self.get_data)
        # 获取数据，子窗体保存按钮
        self.dialog_1.pushButton.clicked.connect(self.get_data)
        # 删除数据，删除按钮
        self.toolButton_2.clicked.connect(self.delete_data)

    def show_dialog(self):
        self.dialog_1.show()
        print('子窗口开启')

    def get_data(self):
        """从数据库获取数据并存入表格"""
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        # 获取数据库数据
        con = sqlite3.connect('命令集.db')
        cursor = con.cursor()
        cursor.execute('select 图像名称,键鼠命令,参数,重复次数,ID from 命令')
        list_order = cursor.fetchall()
        con.close()
        # 在表格中写入数据
        for i in range(len(list_order)):
            self.tableWidget.insertRow(i)
            for j in range(len(list_order[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(list_order[i][j])))

    def delete_data(self):
        """删除选中的数据行"""
        # 删除表中
        try:
            row = self.tableWidget.currentRow()
            xx = self.tableWidget.item(row, 4).text()
            print(xx)
        except AttributeError:
            pass
        try:
            self.tableWidget.removeRow(row)
            # 删除数据库中数据
            con = sqlite3.connect('命令集.db')
            cursor = con.cursor()
            cursor.execute('delete from 命令 where ID=?', (xx,))
            con.commit()
            con.close()
        except UnboundLocalError:
            pass

    def go_up(self):
        """向上移动选中数据"""

class Dialog(QWidget, Ui_Form):
    """添加指令对话框"""

    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.select_file)
        self.spinBox_2.setValue(1)
        self.pushButton.clicked.connect(self.save_data)

    def select_file(self):
        """选择文件夹并返回文件夹名称"""
        filePath = QFileDialog.getExistingDirectory(self, "选择存储目标图像的文件夹")
        images_name = os.listdir(filePath)
        # 去除文件夹中非png文件名称
        for i in range(len(images_name) - 1, -1, -1):
            if ".png" not in images_name[i]:
                images_name.remove(images_name[i])
        print(images_name)
        self.label_6.setText(filePath.split('/')[-1])
        self.comboBox.addItems(images_name)
        self.label_3.setText('无参数')
        self.comboBox_2.currentIndexChanged.connect(self.change_label3)

    def change_label3(self):
        """标签3根据下拉框2的选择变化"""
        self.spinBox_2.setValue(1)
        combox_text = self.comboBox_2.currentText()
        if combox_text == '等待':
            self.label_3.setText('等待时长')
        if combox_text == '左键单击':
            self.label_3.setText('无参数')
        if combox_text == '左键双击':
            self.label_3.setText('无参数')
        if combox_text == '右键单击':
            self.label_3.setText('无参数')

    def save_data(self):
        # 获取4个参数命令
        image = self.comboBox.currentText()
        instruction = self.comboBox_2.currentText()
        parameter = self.spinBox.value()
        repeat_number = self.spinBox_2.value()
        # 连接数据库，将数据插入表中并关闭数据库
        con = sqlite3.connect('命令集.db')
        cursor = con.cursor()
        cursor.execute('INSERT INTO 命令(图像名称,键鼠命令,参数,重复次数) VALUES (?,?,?,?)',
                       (image, instruction, parameter, repeat_number))
        con.commit()
        con.close()
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    main_window = Main_window()
    # 给窗体程序设置图标
    main_window.setWindowIcon(QIcon('图标.ico'))
    # 显示窗体
    main_window.show()
    # 显示添加对话框窗口
    sys.exit(app.exec_())
