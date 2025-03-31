# name: Anbo Xu
# id: 202283890035
''' This program makes the LED light glitter and
 shows its status to the terminal'''

import RPi.GPIO as GPIO
import time
# establish naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("LED on")
# turn the pin 'on' to power the LED light
GPIO.output(18,GPIO.HIGH)
# wait for one second
time.sleep(1)
print("LED off")
# turn the pin 'off' to shutdown supplying power to the LED
GPIO.output(18,GPIO.LOW)
