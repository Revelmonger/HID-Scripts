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
time.sleep(2)

for i in range( 0421 ,9999):
	led.value = True
	string_name = '{0:04}'.format(i)
	for element in string_name:
		if element == "0":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.ZERO)
		elif element == "1":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.ONE)				
		elif element == "2":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.TWO)
		elif element == "3":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.THREE)
		elif element == "4":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.FOUR)
		elif element == "5":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.FIVE)
		elif element == "6":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.SIX)
		elif element == "7":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.SEVEN)
		elif element == "8":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.EIGHT)
		elif element == "9":
			time.sleep(random.randrange(25, 50)/100)
			keyboard.send(Keycode.NINE)
	time.sleep(3)
	keyboard.send(Keycode.E)
	time.sleep(25)











