# The following program captures one still when the push button is pressed, saving the still to the Desktop before exiting the program.

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

buttonPin = 7
buttonPress = True
count = 0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

camera = PiCamera()

while count < 1:
    buttonPress = GPIO.input(buttonPin)
    if buttonPress == False:
        camera.capture("/home/pi/Desktop/picture.jpg")
        count += 1
       
raise SystemExit 

