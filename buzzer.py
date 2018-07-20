import time
import RPi.GPIO as gpio


def buzzer():
	gpio.setwarnings(False)
	gpio.setmode(gpio.BOARD)
	gpio.setup(7, gpio.OUT)

	try:
		while True:
			gpio.output(7,1)
			time.sleep(.1)
			gpio.output(7,0)
			time.sleep(.1)
			exit
	except KeyboardInterrupt:
		gpio.cleanup()
		exit



