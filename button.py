#this is the codes for the Button
#importing of libraries
import paho.mqtt.client as mqtt
from gpiozero import Button
from signal import pause
button = Button(4)

#connection to network
client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

#adding the Location
from geo import getLocation

def button_press():
	print("button clicked")
	client.publish("text/all", "Wavesquad !! " + getLocation())


button.when_pressed = button_press
pause()
