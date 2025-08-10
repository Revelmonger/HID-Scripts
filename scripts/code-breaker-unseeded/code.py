'''
This code.py file is intended to be used as a brute force code breaker
'''
import time
import usb_hid
import os
import board 
import digitalio
import random

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

#Start and stop values to loop through
start_val = 0000
stop_val = 9999

# 10-second delay
time.sleep(10)

# Randomized input delay between keyboard input
input_delay = random.randrange(25, 50)/100

for i in range(start_val, stop_val):
	led.value = True
	string_name = '{0:04}'.format(i)
	for element in string_name:
		if element == "0":
			time.sleep(input_delay)
			keyboard.send(Keycode.ZERO)
		elif element == "1":
			time.sleep(input_delay)
			keyboard.send(Keycode.ONE)				
		elif element == "2":
			time.sleep(input_delay)
			keyboard.send(Keycode.TWO)
		elif element == "3":
			time.sleep(input_delay)
			keyboard.send(Keycode.THREE)
		elif element == "4":
			time.sleep(input_delay)
			keyboard.send(Keycode.FOUR)
		elif element == "5":
			time.sleep(input_delay)
			keyboard.send(Keycode.FIVE)
		elif element == "6":
			time.sleep(input_delay)
			keyboard.send(Keycode.SIX)
		elif element == "7":
			time.sleep(input_delay)
			keyboard.send(Keycode.SEVEN)
		elif element == "8":
			time.sleep(input_delay)
			keyboard.send(Keycode.EIGHT)
		elif element == "9":
			time.sleep(input_delay)
			keyboard.send(Keycode.NINE)
	# Code automatically submitted after typing 4-digits. Add Keycode.ENTER if needing to submit. 
	time.sleep(28) # 28-second delay to prevent lockout
	keyboard.send(Keycode.E) # E-Key used to re-open interface
	time.sleep(2)