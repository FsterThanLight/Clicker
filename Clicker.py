# Copyright (c) [2022] [federalsadler@sohu.com]
# [Clicker] is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
# http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.

import json
import sqlite3

import cryptocode
import requests
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QFileDialog, QTableWidgetItem, QMessageBox, QComboBox, QHeaderView
from 窗体.add_instruction import Ui_Form
from 窗体.mainwindow import Ui_MainWindow
from 窗体.setting import Ui_Setting
from 窗体.about import Ui_Dialog
import sys
import os
from main_work import mainWork, exit_main_work
import time
from PyQt5.QtGui import QDesktopServices

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}


def load_json():
    """从json文件中加载更新网址和保留文件名"""
    file_name = 'update_data.json'
    with open(file_name, 'r', encoding='utf8') as f:
        data = json.load(f)
    url = cryptocode.decrypt(data['url_encrypt'], '123456')
    list_keep = []
    for v in data.values():
        list_keep.append(v)
    # print(url)
    # print(list_keep)
    return url, list_keep[1:]


def get_download_address(main_window, warning):
    """获取下载地址、版本信息、更新说明"""
    global headers
    url, files = load_json()
    print(url)
    try:
        res = requests.get(url, headers=headers, timeout=0.2)
        info = cryptocode.decrypt(res.text, '123456')
        list_1 = info.split('=')
        return list_1[0], list_1[1], list_1[2], list_1[3]
    except requests.exceptions.ConnectionError:
        if warning == 1:
            QMessageBox.critical(main_window, "更新检查", "无法获取更新信息，请检查网络。")
            time.sleep(1)
        else:
            pass


class Main_window(QMainWindow, Ui_MainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)
        # 软件版本
        self.version = 'v0.2'
        # 实例化子窗口1
        self.dialog_1 = Dialog()
        # 实例化设置窗口
        self.setting = Setting()
        # 设置关于窗体
        self.about = About()
        # 设置表格列宽自动变化，并使第5列列宽固定
        self.format_table()
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
        self.tableWidget.cellChanged.connect(lambda:self.table_cell_changed(False))
        # 保存按钮
        self.actionb.triggered.connect(self.save_data_to_current)
        # 清空指令按钮
        self.toolButton_6.clicked.connect(self.clear_table)
        # 导入数据按钮
        self.actionf.triggered.connect(self.data_import)
        # 主窗体开始按钮
        self.pushButton_5.clicked.connect(self.start)
        # 实时计时
        self.lcd_time = 1
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.display_running_time('显示时间'))
        # 打开设置
        self.actions_2.triggered.connect(self.show_setting)
        # 结束任务按钮
        self.pushButton_6.clicked.connect(exit_main_work)
        # 检查更新按钮（菜单栏）
        self.actionj.triggered.connect(lambda: self.check_update(1))
        # 隐藏工具栏
        self.actiong.triggered.connect(self.hide_toolbar)
        # 打开关于窗体
        self.actionabout.triggered.connect(self.show_about)
        # 打开使用说明
        self.actionhelp.triggered.connect(self.open_readme)

    # def keyPressEvent(self, event):
    #     """检测键盘按键事件"""
    #     if event.key()==Qt.Key_Escape:
    #         # 检测到退出键，结束任务
    #         self.start_statu=False
    #         self.textEdit.append('结束任务')

    def show_dialog(self):
        self.dialog_1.show()
        print('子窗口开启')
        resize = self.geometry()
        self.dialog_1.move(resize.x(), resize.y() + 200)

    def format_table(self):
        """设置主窗口表格格式"""
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(4, 50)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(0, 100)

    def show_setting(self):
        self.setting.show()
        self.setting.load_setting_data()
        print('设置窗口打开')
        resize = self.geometry()
        self.setting.move(resize.x() + 90, resize.y())

    def show_about(self):
        """显示关于窗口"""
        self.about.show()
        print('关于窗体开启')
        resize = self.geometry()
        self.about.move(resize.x() + 90, resize.y())

    def get_data(self):
        """从数据库获取数据并存入表格"""
        self.change_state = False
        list_options = ['左键单击', '左键双击', '右键单击', '等待', '滚轮滑动', '内容输入','鼠标移动']
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
                    combox.currentIndexChanged.connect(lambda:self.table_cell_changed(True))
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

    def table_cell_changed(self,combox_change):
        """单元格改变时自动存储"""
        if self.change_state:
            print('自动存储')
            row = self.tableWidget.currentRow()
            if combox_change:
                self.tableWidget.item(row, 2).setText('0')
            else:
                pass
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
            # 退出终止后台进程并清空数据库
            event.accept()
            self.clear_database()
            exit_main_work()
        else:
            event.ignore()

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
        self.dialog_1.filePath = '/'.join(data_file_path[0].split('/')[0:-1])
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
        mainWork(self.dialog_1.filePath, self)

    def clear_plaintext(self, judge):
        """清空处理框中的信息"""
        if judge == 200:
            lines = self.plainTextEdit.blockCount()
            if lines > 200:
                self.plainTextEdit.clear()
        else:
            self.plainTextEdit.clear()

    def display_running_time(self, judge):
        """在主屏幕显示运行时长"""
        if judge == "显示时间":
            self.lcdNumber.display(self.lcd_time)
            self.lcd_time += 1
        elif judge == "开始计时":
            self.timer.start(1000)
        elif judge == "结束计时":
            self.lcd_time = 0
            self.timer.stop()
            self.lcdNumber.display(self.lcd_time)
        elif judge == "暂停计时":
            self.timer.stop()

    def check_update(self, warning):
        """检查更新功能"""
        try:
            address, version, info, name = get_download_address(self, warning)
            print(version)
            if version != self.version:
                x = QMessageBox.information(self, "更新检查", "已发现最新版" + version + "\n是否更新？",
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
                if x == QMessageBox.Yes:
                    print('开始更新')
                    # os.popen()
                    sys.exit()

            else:
                if warning == 1:
                    QMessageBox.information(self, "更新检查", "当前" + self.version + "已是最新版本。")
                else:
                    pass
        except TypeError:
            pass

    def main_show(self):
        """显示窗体，并根据设置检查更新"""
        self.show()
        import sqlite3
        # 连接数据库获取是否检查更新选项
        con = sqlite3.connect('命令集.db')
        cursor = con.cursor()
        cursor.execute('select 值 from 设置 where 设置类型=?', ('启动检查更新',))
        x = cursor.fetchall()[0][0]
        cursor.close()
        print('启动检查更新')
        print(x)
        if x == 1:
            self.check_update(0)
        else:
            pass

    def hide_toolbar(self):
        """隐藏工具栏"""
        if self.actiong.isChecked():
            self.toolBar.show()
        elif not self.actiong.isChecked():
            self.toolBar.hide()

    def open_readme(self):
        """打开使用说明"""
        os.popen('README.pdf')


class Dialog(QWidget, Ui_Form):
    """添加指令对话框"""

    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)
        self.pushButton_3.clicked.connect(lambda: self.select_file(0))
        self.spinBox_2.setValue(1)
        self.pushButton.clicked.connect(self.save_data)
        self.filePath = ''
        # 设置子窗口出现阻塞主窗口
        self.setWindowModality(Qt.ApplicationModal)
        self.list_combox_3_value = []
        list_controls = [self.textEdit, self.spinBox, self.spinBox_2, self.comboBox,
                         self.comboBox_3]
        for i in list_controls:
            i.setEnabled(False)

    def select_file(self, judge):
        """选择文件夹并返回文件夹名称"""
        if judge == 0:
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
        self.comboBox_2.currentIndexChanged.connect(self.change_label3)
        self.comboBox.setEnabled(True)
        self.spinBox_2.setEnabled(True)

    def change_label3(self):
        """标签3根据下拉框2的选择变化"""
        self.spinBox_2.setValue(1)
        combox_text = self.comboBox_2.currentText()

        def commonly_used_controls(dialog_1):
            """常用控件恢复运行"""
            dialog_1.label_2.setStyleSheet('color:red')
            dialog_1.comboBox.setEnabled(True)
            dialog_1.spinBox_2.setEnabled(True)
            dialog_1.label_4.setStyleSheet('color:red')

        def all_disabled(dialog_1):
            """指令框所有控件全部禁用"""
            list_controls = [dialog_1.textEdit, dialog_1.spinBox, dialog_1.spinBox_2, dialog_1.comboBox,
                             dialog_1.comboBox_3]
            list_label = [dialog_1.label_2, dialog_1.label_3, dialog_1.label_4, dialog_1.label_7,
                          dialog_1.label_8]
            for i in list_controls:
                i.setEnabled(False)
            for i in list_label:
                i.setStyleSheet('color:transparent')
            dialog_1.comboBox_3.clear()

        if combox_text == '等待':
            all_disabled(self)
            commonly_used_controls(self)
            self.label_3.setStyleSheet('color:red')
            self.spinBox.setEnabled(True)
            self.label_3.setText('等待时长')

        if combox_text == '左键单击':
            all_disabled(self)
            commonly_used_controls(self)

        if combox_text == '左键双击':
            all_disabled(self)
            commonly_used_controls(self)

        if combox_text == '右键单击':
            all_disabled(self)
            commonly_used_controls(self)

        if combox_text == '滚轮滑动':
            all_disabled(self)
            commonly_used_controls(self)
            self.label_3.setStyleSheet('color:red')
            self.label_3.setText('滑动距离')
            self.label_8.setStyleSheet('color:red')
            self.label_8.setText('滑动方向')
            self.list_combox_3_value = ['向上滑动', '向下滑动']
            self.comboBox_3.addItems(self.list_combox_3_value)
            self.comboBox_3.setEnabled(True)
            self.spinBox.setEnabled(True)

        if combox_text == '内容输入':
            all_disabled(self)
            commonly_used_controls(self)
            self.label_7.setStyleSheet('color:red')
            self.textEdit.setEnabled(True)

        if combox_text == '鼠标移动':
            all_disabled(self)
            commonly_used_controls(self)
            self.label_8.setStyleSheet('color:red')
            self.label_8.setText('移动方向')
            self.label_3.setStyleSheet('color:red')
            self.label_3.setText('移动距离')
            self.list_combox_3_value = ['向上', '向下', '向左', '向右']
            self.comboBox_3.addItems(self.list_combox_3_value)
            self.comboBox_3.setEnabled(True)
            self.spinBox.setEnabled(True)

    def save_data(self):
        """获取4个参数命令"""
        instruction = self.comboBox_2.currentText()
        # 根据参数的不同获取不同位置的4参数
        # 获取图像名称和重读次数
        image = self.comboBox.currentText()
        repeat_number = self.spinBox_2.value()
        parameter = ''
        # 获取鼠标单击事件或等待的参数
        list_click = ['左键单击', '左键双击', '右键单击', '等待']
        if instruction in list_click:
            parameter = self.spinBox.value()
        # 获取滚轮滑动事件参数
        if instruction == '滚轮滑动':
            direction = self.comboBox_3.currentText()
            if direction == '向上滑动':
                parameter = self.spinBox.value()
            elif direction == '向下滑动':
                x = int(self.spinBox.value())
                parameter = str(x - 2 * x)
        # 获取内容输入事件的参数
        if instruction == '内容输入':
            parameter = self.textEdit.toPlainText()
        # 获取鼠标移动的事件参数
        if instruction=='鼠标移动':
            direction = self.comboBox_3.currentText()
            distance=self.spinBox.value()
            parameter=direction+'-'+str(distance)
        # 连接数据库，将数据插入表中并关闭数据库
        con = sqlite3.connect('命令集.db')
        cursor = con.cursor()
        cursor.execute('INSERT INTO 命令(图像名称,键鼠命令,参数,重复次数) VALUES (?,?,?,?)',
                       (image, instruction, parameter, repeat_number))
        con.commit()
        con.close()
        self.close()


class Setting(QWidget, Ui_Setting):
    """添加设置窗口"""

    def __init__(self):
        super().__init__()
        # 初始化窗体
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        # 点击保存（应用）按钮
        self.pushButton.clicked.connect(self.save_setting)
        # 点击恢复至默认按钮
        self.pushButton_3.clicked.connect(self.restore_default)
        # 开启极速模式
        self.radioButton_2.clicked.connect(self.speed_mode)
        # 切换普通模式
        self.radioButton.clicked.connect(self.normal_mode)

    def save_setting_date(self):
        """保存设置数据"""
        # 重窗体控件提取数据并放入列表
        list_setting_name = ['图像匹配精度', '时间间隔', '持续时间', '暂停时间', '模式', '启动检查更新']
        image_accuracy = self.horizontalSlider.value() / 10
        interval = self.horizontalSlider_2.value() / 1000
        duration = self.horizontalSlider_3.value() / 1000
        time_sleep = self.horizontalSlider_4.value() / 1000
        model = 1
        if self.checkBox.isChecked():
            update_check = 1
        else:
            update_check = 0
        if self.radioButton_2.isChecked():
            model = 2
        list_setting_value = [image_accuracy, interval, duration, time_sleep, model, update_check]
        # 打开数据库并更新设置数据
        con = sqlite3.connect('命令集.db')
        cursor = con.cursor()
        for i in range(len(list_setting_name)):
            cursor.execute("update 设置 set 值=? where 设置类型=?", (list_setting_value[i], list_setting_name[i]))
            con.commit()
        con.close()

    def save_setting(self):
        """保存按钮事件"""
        self.save_setting_date()
        QMessageBox.information(self, '提醒', '保存成功！')
        self.close()

    def restore_default(self):
        """设置恢复至默认"""
        self.radioButton.isChecked()
        self.horizontalSlider.setValue(9)
        self.horizontalSlider_2.setValue(200)
        self.horizontalSlider_3.setValue(200)
        self.horizontalSlider_4.setValue(100)
        self.save_setting_date()

    def load_setting_data(self):
        """加载设置数据库中的数据"""
        # 连接数据库存入列表
        con = sqlite3.connect('命令集.db')
        cursor = con.cursor()
        cursor.execute('select * from 设置')
        list_setting_data = cursor.fetchall()
        con.close()
        print(list_setting_data)
        # 设置控件数据为数据库保存的数据
        self.horizontalSlider.setValue(int(list_setting_data[0][1] * 10))
        self.horizontalSlider_2.setValue(int(list_setting_data[1][1] * 1000))
        self.horizontalSlider_3.setValue(int(list_setting_data[2][1] * 1000))
        self.horizontalSlider_4.setValue(int(list_setting_data[3][1] * 1000))
        # 极速模式
        if int(list_setting_data[4][1]) == 2:
            self.radioButton_2.setChecked(True)
            self.pushButton_3.setEnabled(False)
            self.horizontalSlider_2.setEnabled(False)
            self.horizontalSlider_4.setEnabled(False)
        if list_setting_data[5][1] == 1:
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

    def speed_mode(self):
        """极速模式开启"""
        self.horizontalSlider_2.setValue(0)
        self.horizontalSlider_3.setValue(100)
        self.horizontalSlider_4.setValue(0)
        self.horizontalSlider_2.setEnabled(False)
        self.horizontalSlider_4.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.save_setting_date()

    def normal_mode(self):
        """切换普通模式"""
        self.horizontalSlider_2.setEnabled(True)
        self.horizontalSlider_4.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.save_setting_date()


class About(QWidget, Ui_Dialog):
    """关于窗体"""

    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)
        # 去除窗体最大化、最小化按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.github.clicked.connect(self.show_github)
        self.gitee.clicked.connect(self.show_gitee)

    def show_github(self):
        QDesktopServices.openUrl(QUrl('https://github.com/FsterThanLight/Clicker'))

    def show_gitee(self):
        QDesktopServices.openUrl(QUrl('https://gitee.com/fasterthanlight/automatic_clicker'))


if __name__ == "__main__":
    app = QApplication([])
    main_window = Main_window()
    # 显示窗体，并根据设置检查更新
    main_window.main_show()
    # 显示添加对话框窗口
    sys.exit(app.exec_())
