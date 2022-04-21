# Copyright (c) [2022] [federalsadler@sohu.com]
# [Clicker] is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
# http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.

import sqlite3
import time
import keyboard
import pyautogui
import pyperclip
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
import threading
import sys
from setting import SettingsData

start_state = True
suspended = True
event = threading.Event()


def exit_main_work():
    sys.exit()


def real_time_display_status(main_window):
    """设置实时显示状态文本"""
    QApplication.processEvents()
    # 当信息超过200行则清空
    main_window.clear_plaintext(200)


def execute_click(click_times, lOrR, img, main_window, number, setting):
    """执行鼠标点击事件"""
    # 4个参数：鼠标点击时间，按钮类型（左键右键中键），图片名称，重复次数
    location = pyautogui.locateCenterOnScreen(img, confidence=setting.confidence)
    if location is not None:
        # 参数：位置X，位置Y，点击次数，时间间隔，持续时间，按键
        pyautogui.click(location.x, location.y,
                        clicks=click_times, interval=setting.interval, duration=setting.duration, button=lOrR)
        main_window.plainTextEdit.appendPlainText('执行鼠标点击' + str(number))
        real_time_display_status(main_window)
    else:
        main_window.plainTextEdit.appendPlainText('未匹配到图片' + str(number))
        real_time_display_status(main_window)
        print('未找到匹配图片' + str(number))


def mouse_moves(direction, distance, main_window, setting):
    """鼠标移动事件"""
    # 显示鼠标当前位置
    x, y = pyautogui.position()
    print('x:' + str(x) + ',y:' + str(y))
    # 相对于当前位置移动鼠标
    if direction == '向上':
        pyautogui.moveRel(0, -abs(int(distance)), duration=setting.duration)
    elif direction == '向下':
        pyautogui.moveRel(0, int(distance), duration=setting.duration)
    elif direction == '向左':
        pyautogui.moveRel(-abs(int(distance)), 0, duration=setting.duration)
    elif direction == '向右':
        pyautogui.moveRel(int(distance), 0, duration=setting.duration)
    main_window.plainTextEdit.appendPlainText('移动鼠标' + direction + distance + '距离')
    real_time_display_status(main_window)


def wheel_slip(scroll, main_window, setting):
    """滚轮滑动事件"""
    pyautogui.scroll(scroll)
    main_window.plainTextEdit.appendPlainText('滚轮滑动' + str(scroll) + '距离')
    real_time_display_status(main_window)


def text_input(input_value, main_window, setting):
    """文本输入事件"""
    pyperclip.copy(input_value)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(setting.time_sleep)
    main_window.plainTextEdit.appendPlainText('执行文本输入')


def execution_repeats(cmd_type, list_ins, reTry, main_window, number, setting):
    """执行重复次数"""

    def determine_execution_type(cmd_type, list_ins, main_window, number, setting):
        """执行判断命令类型并调用对应函数"""
        if cmd_type == '左键单击' or cmd_type == '右键单击' or cmd_type == '左键双击':
            click_times = list_ins[0]
            lOrR = list_ins[1]
            img = list_ins[2]
            execute_click(click_times, lOrR, img, main_window, number, setting)
        elif cmd_type == '鼠标移动':
            direction = list_ins[0]
            distance = list_ins[1]
            mouse_moves(direction, distance, main_window, setting)
        elif cmd_type == '滚轮滑动':
            scroll = list_ins[0]
            wheel_slip(scroll, main_window, setting)
        elif cmd_type == '内容输入':
            input_value = list_ins[0]
            text_input(input_value, main_window, setting)

    if reTry == 1:
        # 参数：图片和查找精度，返回目标图像在屏幕的位置
        determine_execution_type(cmd_type, list_ins, main_window, number, setting)
    elif reTry > 1:
        # 有限次重复
        i = 1
        while i < reTry + 1:
            determine_execution_type(cmd_type, list_ins, main_window, number, setting)
            i += 1
            time.sleep(setting.time_sleep)
    else:
        pass


def execute_instructions(file_path, list_instructions, main_window, number, setting):
    """执行收到的指令"""
    for i in range(len(list_instructions)):
        # 读取指令
        cmd_type = list_instructions[i][2]
        re_try = list_instructions[i][4]
        if cmd_type == '左键单击':
            # 取图片名称
            img = (file_path + "/" + list_instructions[i][1]).replace('/', '//')
            # 取重复次数
            re_try = list_instructions[i][4]
            # 调用鼠标点击事件
            list_ins = [1, 'left', img]
            execution_repeats(cmd_type, list_ins, re_try, main_window, number, setting)
        elif cmd_type == '左键双击':
            img = (file_path + "/" + list_instructions[i][1]).replace('/', '//')
            re_try = list_instructions[i][4]
            list_ins = [2, 'left', img]
            execution_repeats(cmd_type, list_ins, re_try, main_window, number, setting)
        elif cmd_type == '右键单击':
            img = (file_path + "/" + list_instructions[i][1]).replace('/', '//')
            re_try = list_instructions[i][4]
            list_ins = [1, 'right', img]
            execution_repeats(cmd_type, list_ins, re_try, main_window, number, setting)
        elif cmd_type == '等待':
            wait_time = int(list_instructions[i][3])
            main_window.plainTextEdit.appendPlainText('等待时长' + str(wait_time) + '秒')
            time.sleep(wait_time)
        elif cmd_type == '滚轮滑动':
            scroll = int(list_instructions[i][3])
            list_ins = [scroll]
            execution_repeats(cmd_type, list_ins, re_try, main_window, number, setting)
        elif cmd_type == '内容输入':
            input_value = str(list_instructions[i][3])
            list_ins = [input_value]
            execution_repeats(cmd_type, list_ins, re_try, main_window, number, setting)
        elif cmd_type == '鼠标移动':
            direction = str(list_instructions[i][3]).split('-')[0]
            distance = str(list_instructions[i][3]).split('-')[1]
            list_ins = [direction, distance]
            execution_repeats(cmd_type, list_ins, re_try, main_window, 0, setting)


def mainWork(file_path, main_window):
    """参数为图片名称"""
    global start_state, suspended
    # 设置终止状态为true，暂停功能为false
    start_state = True
    suspended = False
    if main_window.checkBox_2.isChecked():
        main_window.hide()
    # 获取设置参数，初始化
    setting = SettingsData()
    setting.init()
    # 获取数据库中存储的指令
    con = sqlite3.connect('命令集.db')
    cursor = con.cursor()
    cursor.execute('select * from 命令')
    list_instructions = cursor.fetchall()
    con.close()
    # 执行数据库指令
    if len(list_instructions) != 0:
        try:
            # 检测主窗体无限循环按钮是否选中，并执行命令
            keyboard.hook(abc)
            if main_window.radioButton.isChecked():
                main_window.display_running_time('开始计时')
                # 在窗体中显示循环次数
                number = 1
                while start_state:
                    # 如果状态为True执行无限循环
                    execute_instructions(file_path, list_instructions, main_window, number, setting)
                    if not start_state:
                        main_window.plainTextEdit.appendPlainText('结束任务')
                        main_window.display_running_time('结束计时')
                        break
                    if suspended:
                        event.clear()
                        event.wait(86400)
                    number += 1
                    time.sleep(setting.time_sleep)
                if main_window.checkBox_2.isChecked():
                    print('窗体出现')
                    main_window.show()
            elif main_window.radioButton_2.isChecked():
                main_window.display_running_time('开始计时')
                number = 1
                # 如果状态为有限次循环
                repeat_number = main_window.spinBox.value()
                while number <= repeat_number and start_state:
                    execute_instructions(file_path, list_instructions, main_window, number, setting)
                    if not start_state:
                        main_window.show()
                        main_window.plainTextEdit.appendPlainText('结束任务')
                        main_window.display_running_time('结束计时')
                        break
                    if suspended:
                        event.clear()
                        event.wait(86400)
                    number += 1
                    time.sleep(setting.time_sleep)
                main_window.plainTextEdit.appendPlainText('结束任务')
                if main_window.checkBox_2.isChecked():
                    print('窗体出现')
                    main_window.show()
                main_window.display_running_time('结束计时')
            elif not main_window.radioButton.isChecked() and not main_window.radioButton_2.isChecked():
                QMessageBox.information(main_window, "提示", "请设置执行循环次数！")
        except OSError:
            QMessageBox.critical(main_window, '错误', '目标图像文件夹或图片命名暂不支持中文！')


def abc(x):
    """键盘事件，退出任务、开始任务、暂停恢复任务"""
    global start_state, suspended
    a = keyboard.KeyboardEvent('down', 1, 'esc')
    s = keyboard.KeyboardEvent('down', 31, 's')
    r = keyboard.KeyboardEvent('down', 19, 'r')
    # var = x.scan_code
    # print(var)
    if x.event_type == 'down' and x.name == a.name:
        print("你按下了退出键")
        start_state = False
    if x.event_type == 'down' and x.name == s.name:
        print("你按下了暂停键")
        suspended = True
    if x.event_type == 'down' and x.name == r.name:
        print('你按下了恢复键')
        event.set()
        suspended = False
