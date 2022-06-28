import RPi.GPIO as gpio
import time
from evdev import InputDevice
import sys

##Function for reading input data from bluetooth device
##bluetooth device for this pllication has a single button
##Function returns True id button is pressed
def read_loop(button):
	value = False
	for event in button.read_loop():
		if event:
			value = True
			return value

#Setting board configuration
gpio.setmode(gpio.BOARD)
gpio.setup(16, gpio.OUT)
#gpio.setup(40, gpio.OUT, initial=gpio.LOW)

#To Check Bluetooth Connection and allow time to connect
for x in range(0,5):
	try:
		blue_button = InputDevice('/dev/input/event0')

	except Exception as e:
		time.sleep(10)

#Visual Indication for bluetooth connection
if blue_button:
	gpio.output(16, gpio.HIGH) #LED
	time.sleep(3)
	gpio.output(16, gpio.LOW)
	time.sleep(0.1)
else:
	for x in range(0,2): #LED Blinks and exits program if no connection
		gpio.output(16, gpio.HIGH)
		time.sleep(0.1)
		gpio.output(16, gpio.LOW)
		time.sleep(0.1)
	sys.exit()

gpio.output(16, gpio.HIGH)

gpio.setup(40, gpio.OUT, initial = gpio.HIGH)

while 1:
	button_press = read_loop(blue_button)
	if button_press:
		gpio.output(40, gpio.LOW)
		time.sleep(0.4)
		gpio.output(40, gpio.HIGH)
	#gpio.cleanup()
