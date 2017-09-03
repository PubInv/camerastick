# Morgan, paste your code here.
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

buttonPin = 7

buttonPress = True

GPIO.setmode(GPIO.BOARD)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

camera = PiCamera()

while True:
    buttonPress = GPIO.input(buttonPin)
    if buttonPress == False:
        camera.capture("/home/pi/Desktop/picture.jpg")

