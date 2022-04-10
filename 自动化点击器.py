import pyautogui
import pyperclip
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QFileDialog, QTableWidgetItem, QMessageBox, QComboBox, QHeaderView
from 窗体.add_instruction import Ui_Form
from 窗体.mainwindow import Ui_MainWindow
import sys
import os
from main_work import mainWork
import time


class Main_window(QMainWindow, Ui_MainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)
        # 实例化子窗口1
        self.dialog_1 = Dialog()
        # 设置表格列宽自动变化，并使第5列列宽固定
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(4, 50)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(0, 100)
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
        # 交换数据，上移按钮
        self.toolButton_3.clicked.connect(lambda: self.go_up_down("up"))
        self.toolButton_4.clicked.connect(lambda: self.go_up_down("down"))
        # 单元格变动自动存储
        self.change_state = True
        self.tableWidget.cellChanged.connect(self.table_cell_changed)
        # 保存按钮
        self.actionb.triggered.connect(self.save_data_to_current)
        # 清空指令按钮
        self.toolButton_6.clicked.connect(self.clear_table)
        # 导入数据按钮
        self.actionf.triggered.connect(self.data_import)
        # 主窗体开始按钮
        self.start_statu=False
        self.pushButton_5.clicked.connect(self.start)

    # def keyPressEvent(self, event):
    #     """检测键盘按键事件"""
    #     if event.key()==Qt.Key_Escape:
    #         # 检测到退出键，结束任务
    #         self.start_statu=False
    #         self.textEdit.append('结束任务')

    def show_dialog(self):
        self.dialog_1.show()
        print('子窗口开启')

    def get_data(self):
        """从数据库获取数据并存入表格"""
        self.change_state = False
        list_options = ['左键单击', '左键双击', '右键单击', '等待']
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
                if j != 1:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(list_order[i][j])))
                else:
                    combox = QComboBox()
                    combox.addItems(list_options)
                    combox.setCurrentText(list_order[i][j])
                    self.tableWidget.setCellWidget(i, 1, combox)
                    combox.currentIndexChanged.connect(self.table_cell_changed)
        self.change_state = True

    def delete_data(self):
        """删除选中的数据行"""
        # 删除表中
        row = self.tableWidget.currentRow()
        if row != -1:
            xx = self.tableWidget.item(row, 4).text()
        else:
            xx = -1
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

    def go_up_down(self, judge):
        """向上移动选中数据"""
        # 获取选中值的行号和id
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        try:
            id = int(self.tableWidget.item(row, 4).text())
            if judge == 'up':
                id_up_down = id - 1
                row_up_down = row - 1
            else:
                id_up_down = id + 1
                row_up_down = row + 1
            # 连接数据库
            con = sqlite3.connect('命令集.db')
            cursor = con.cursor()
            cursor.execute('select 图像名称,键鼠命令,参数,重复次数 from 命令 where ID=?', (id,))
            list_id = cursor.fetchall()
            cursor.execute('select 图像名称,键鼠命令,参数,重复次数 from 命令 where ID=?', (id_up_down,))
            list_id_up = cursor.fetchall()
            # 更新数据库，交换两行数据，保持id不变
            try:
                cursor.execute('update 命令 set 图像名称=?,键鼠命令=?,参数=?,重复次数=? where ID=?',
                               (list_id[0][0], list_id[0][1], list_id[0][2], list_id[0][3], id_up_down))
                con.commit()
                cursor.execute('update 命令 set 图像名称=?,键鼠命令=?,参数=?,重复次数=? where ID=?',
                               (list_id_up[0][0], list_id_up[0][1], list_id_up[0][2], list_id_up[0][3], id))
                con.commit()
                self.get_data()
                self.tableWidget.setCurrentCell(row_up_down, column)
            except IndexError:
                pass
        except AttributeError:
            pass

    def table_cell_changed(self):
        """单元格改变时自动存储"""
        if self.change_state:
            print('自动存储')
            row = self.tableWidget.currentRow()
            # 获取选中行的id，及其他参数
            id = self.tableWidget.item(row, 4).text()
            images = self.tableWidget.item(row, 0).text()
            parameter = self.tableWidget.item(row, 2).text()
            repeat_number = self.tableWidget.item(row, 3).text()
            option = self.tableWidget.cellWidget(row, 1).currentText()
            # 连接数据库，提交修改
            con = sqlite3.connect('命令集.db')
            cursor = con.cursor()
            cursor.execute('update 命令 set 图像名称=?,键鼠命令=?,参数=?,重复次数=? where ID=?',
                           (images, option, parameter, repeat_number, id))
            con.commit()
            con.close()

    def save_data_to_current(self):
        """保存配置文件到当前文件夹下"""
        if self.dialog_1.filePath != '':
            file = self.dialog_1.filePath + "/命令集.txt"
            with open(file, 'w', encoding='utf-8') as f:
                f.write('请将本文件放入保存图像的文件夹中。\n')
                con = sqlite3.connect('命令集.db')
                cursor = con.cursor()
                cursor.execute('select * from 命令')
                list_orders = cursor.fetchall()
                con.close()
                # txt中写入数据
                for i in range(len(list_orders)):
                    for j in range(len(list_orders[i])):
                        f.write(str(list_orders[i][j]) + ',')
                    f.write('\n')
                QMessageBox.information(self, '保存成功', '数据已保存至' + file)
        else:
            QMessageBox.warning(self, '未选择文件夹', "请点击'添加指令'并选择存放目标图像的文件夹！")

    def clear_database(self):
        """清空数据库"""
        con = sqlite3.connect('命令集.db')
        cursor = con.cursor()
        cursor.execute('delete from 命令 where ID<>-1')
        con.commit()
        con.close()

    def closeEvent(self, event):
        choice = QMessageBox.question(self, "提示", "确定退出并清空所有指令？")
        if choice == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        self.clear_database()

    def clear_table(self):
        """清空表格和数据库"""
        choice = QMessageBox.question(self, "提示", "确认清除所有指令吗？")
        if choice == QMessageBox.Yes:
            self.clear_database()
            self.get_data()
        else:
            pass

    def data_import(self):
        """导入数据功能"""
        data_file_path = QFileDialog.getOpenFileName(self, "请选择'命令集.txt'", '', "(*.txt)")
        # 获取命令集文件夹路径
        self.dialog_1.filePath='/'.join(data_file_path[0].split('/')[0:-1])
        self.dialog_1.select_file(1)
        # 清空数据库并导入新数据
        if data_file_path[0] != '':
            self.clear_database()
            with open(data_file_path[0], 'r', encoding='utf-8') as f:
                list_order = f.readlines()
                print(list_order)
                for i in list_order:
                    j = i.split(',')
                    if len(j) == 6:
                        # 将txt文本转化为数据库对应参数
                        id = int(j[0])
                        image_name = j[1]
                        instruction = j[2]
                        parameter = j[3]
                        repeat_number = int(j[4])
                        # 连接数据库，插入数据
                        con = sqlite3.connect('命令集.db')
                        cursor = con.cursor()
                        try:
                            cursor.execute('insert into 命令(ID,图像名称,键鼠命令,参数,重复次数) values(?,?,?,?,?)',
                                       (id, image_name, instruction, parameter, repeat_number))
                        except sqlite3.IntegrityError:
                            pass
                        con.commit()
                        con.close()
            self.get_data()

    def start(self):
        """主窗体开始按钮"""
        self.plainTextEdit.setPlaceholderText('开始任务')
        mainWork(self.dialog_1.filePath,self)


class Dialog(QWidget, Ui_Form):
    """添加指令对话框"""

    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)
        self.pushButton_3.clicked.connect(lambda:self.select_file(0))
        self.spinBox_2.setValue(1)
        self.pushButton.clicked.connect(self.save_data)
        self.filePath = ''
        # 设置子窗口出现阻塞主窗口
        self.setWindowModality(Qt.ApplicationModal)

    def select_file(self,judge):
        """选择文件夹并返回文件夹名称"""
        if judge==0:
            self.filePath = QFileDialog.getExistingDirectory(self, "选择存储目标图像的文件夹")
        try:
            images_name = os.listdir(self.filePath)
        except FileNotFoundError:
            images_name = []
        # 去除文件夹中非png文件名称
        for i in range(len(images_name) - 1, -1, -1):
            if ".png" not in images_name[i]:
                images_name.remove(images_name[i])
        print(images_name)
        self.label_6.setText(self.filePath.split('/')[-1])
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
