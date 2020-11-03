from pyautogui import *
import pyautogui
import keyboard
import time
import random
import win32api, win32con

# Tile 1 = X: 800 Y: 650 RGB: ( 36, 37, 37)
# Tile 2 = X: 900 Y: 650 RGB: ( 36, 37, 37)
# Tile 3 = X: 1000 Y: 650 RGB: ( 36, 37, 37)
# Tile 4 = X: 1100 Y: 650 RGB: ( 36, 37, 37)

x1 = 800
x2 = 900
x3 = 1000
x4 = 1100
y1 = 650

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(x1, y1)[0] == 17:
        click(x1,y1)
    if pyautogui.pixel(x2, y1)[0] == 17:
        click(x2,y1)
    if pyautogui.pixel(x3, y1)[0] == 17:
        click(x3,y1)
    if pyautogui.pixel(x4, y1)[0] == 17:
        click(x4,y1)
