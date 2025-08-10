'''
This code.py is intended to mess with people
'''
import time
import usb_hid
import os

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# 3-minute delay
time.sleep(180)

keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)
layout.write("http://tinyurl.com/s63ve48\n")
time.sleep(2)
keyboard.send(Keycode.F)