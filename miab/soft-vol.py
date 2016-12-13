# Volume control script
# (c) Copyright 2016 Museum in a Box Ltd
#
import RPi.GPIO as GPIO
from subprocess import check_output

# Number of milliseconds to use for debouncing button presses
debounce = 30

# Volume levels
minVol = 0
maxVol = 100
volStep = 15

# Pin assignments
GPIO.setmode(GPIO.BCM)
volUpPin = 6
volDownPin = 13

# Set up pins
GPIO.setup(volUpPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(volDownPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Callback 
def vol_callback(chan):
    current_vol = int(check_output("amixer cget numid=1 | grep values | grep -v type | cut -d '=' -f 2 | cut -d ',' -f 1", shell=True))
    #print(current_vol)
    if chan == volUpPin:
        check_output("amixer cset numid=1 -- " + str(current_vol + volStep), shell=True)
    else:
        check_output("amixer cset numid=1 -- " + str(current_vol - volStep), shell=True)

GPIO.add_event_detect(volUpPin, GPIO.FALLING, callback=vol_callback, bouncetime=debounce)
GPIO.add_event_detect(volDownPin, GPIO.FALLING, callback=vol_callback, bouncetime=debounce)

while 1:
  True
