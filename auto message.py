# 1st "pip install pywhatkit" "pip install PyAutoGUI" "pip install pyperclip" in terminal
import pyautogui
import pyperclip
import time


def workaround_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')


time.sleep(3)
a = 1
while a <= 100:
    workaround_write(str(a) + " Hello world")
    time.sleep(0.5)
    pyautogui.press("enter")
    a += 1
