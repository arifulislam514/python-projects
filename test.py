# 1st "pip install pywhatkit" "pip install PyAutoGUI" in terminal
"""
import pyautogui
import time
time.sleep(4)
while True:
    #time.sleep(1)
    pyautogui.typewrite("Hello world!")
    pyautogui.press("enter")
"""
if __name__ == '__main__':
    n = int(input())
    x=0
    for i in range(1, n+1):
        x+=str(i)

    print(x)
    