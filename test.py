import threading
import keyboard

def abc(x):
    """键盘事件，退出任务、开始任务、暂停恢复任务"""
    b = keyboard.KeyboardEvent('down', 31, 'space')
    if x.event_type == 'down' and x.name == b.name:
        print("你按下了退出键")
        event.set()

keyboard.hook(abc)
event = threading.Event()
print('...部分代码...')
event.wait(10)
print('...剩下的代码...')
