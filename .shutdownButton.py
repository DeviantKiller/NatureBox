#!/bin/python
# Deviant Killer  - Code used for GPIO shutdown  to run separate to main script.
# FInstructions as followed:

# use  a 10k resistor between 3.3v and switch
# use a 1k resistor between GPIO.IN and switch and 3.3v
# use other pin to ground

# sudo nano /etc/rc.local
# Put before the exit 0 line:
# python /home/pi/.shutdownButton.py
# Or for multiple scripts.
# python /home/pi/.shutdownButton.py & otherscript.py

import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(25, GPIO.FALLING)
    os.system("sudo shutdown -h now")
except:
    pass

GPIO.cleanup()
#GPIO Cleanup
