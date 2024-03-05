'''
This code.py file is intended to be used as an autoclicker
'''
import time
import usb_hid
import board 
import digitalio

from adafruit_hid.mouse import Mouse


mouse = Mouse(usb_hid.devices)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

time.sleep(15)

while True:
	led.value = True
	mouse.click(Mouse.LEFT_BUTTON)
	time.sleep(.1)







