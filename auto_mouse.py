import win32api as api
import win32con
import psutil

import time
WINDOW_W = api.GetSystemMetrics(0)
WINDOW_H = api.GetSystemMetrics(1)

print("Width = ", WINDOW_W)
print("Height = ", WINDOW_H)

WIN_MENU_W = WINDOW_W - (WINDOW_W - 25)
WIN_MENU_H = WINDOW_H - 25


BTN_CODE = {
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
    }

def mouse_clicker(x, y):
    api.SetCursorPos((x,y))
    api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(1)
    print('mouse done')

def keyboard_press(*args):
    for b in args:
        api.keybd_event(BTN_CODE[b], 0,0,0)
        time.sleep(0.2)
        api.keybd_event(BTN_CODE[b], 0 , win32con.KEYEVENTF_KEYUP, 0)



for p in psutil.process_iter(): 
    if p.name() in ['opera.exe','firefox.exe','google.exe','yandex.exe']:
        print(p)
else:
    print('нет процесса')

print(api.GetSystemMetrics(80))
print(api.GetSystemMetrics(15))
print(api.GetSystemMetrics(0))
print(api.GetSystemMetrics(11))

BR_POS = [65, 325]

#mouse_clicker(WIN_MENU_W, WIN_MENU_H)
#mouse_clicker(WIN_MENU_W, WIN_MENU_H - 50)
#keyboard_press("b","r","o","w","s","e","r")

#mouse_clicker(BR_POS[0],BR_POS[1])