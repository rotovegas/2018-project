import paho.mqtt.client as mqtt
from gpiozero import Button
from signal import pause
button = Button(4)

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)


def button_press():
	print("button clicked")
	client.publish("text/all", "Wavesquad !!")


button.when_pressed = button_press
pause()