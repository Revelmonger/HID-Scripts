import time
import usb_hid
import os
import board
import digitalio
import random
import re

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

time.sleep(2)

with open('file.txt') as input_file:
    for i, line in enumerate(input_file):
        sep = ','
        stripped = line.split(sep, 1)[0]
        for element in stripped:
            if element == "0":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.ZERO)
            elif element == "1":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.ONE)
            elif element == "2":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.TWO)
            elif element == "3":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.THREE)
            elif element == "4":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.FOUR)
            elif element == "5":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.FIVE)
            elif element == "6":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.SIX)
            elif element == "7":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.SEVEN)
            elif element == "8":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.EIGHT)
            elif element == "9":
                time.sleep(random.randrange(50, 100) / 500)
                keyboard.send(Keycode.NINE)
        time.sleep(26)
        time.sleep(2)
        keyboard.send(Keycode.E)
        time.sleep(2)
