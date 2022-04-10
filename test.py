import pyautogui

# x=pyautogui.locateCenterOnScreen('b.png')
# x = pyautogui.locateCenterOnScreen(f'C:\\Users\\23096\Desktop\Automatic_clicker\\目标图像\\a.png')
# print(x)
# y = input()

# location = pyautogui.locateOnScreen('./images/a.png')
location = pyautogui.locateOnScreen(r"C:\\Users\\23096\\Desktop\\Automatic_clicker\\images\\a.png")
# file_path = unicode('八.bmp', "utf8")
x=pyautogui.center(location)
print(x)
y=input()
