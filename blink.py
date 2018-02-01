# Description: for blinking light on raspberry pi.
# starting with quartoknows code, and modifying (in other files).
#
# Coding Club 25 Jan 2018 and again 1 Feb 2018
#
# Resources:
#  - https://www.quartoknows.com/page/raspberry-pi-blinking-led

import RPi.GPIO as GPIO
from time import sleep



LED_GPIO = 4

print("Getting ready...")

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GPIO, GPIO.OUT)

def set_led(state):
    if state:
        GPIO.output(LED_GPIO, False)
    else:
        GPIO.output(LED_GPIO, True)

# what will happen if we change the value sent to sleep?
set_led(False)
print("LED is ON")
sleep(2)

set_led(True)
print("LED is OFF")
sleep(2)

set_led(False)
print("LED is ON")
sleep(2)

set_led(True)
print("LED is OFF")
sleep(2)

set_led(False)
print("Turning it on finally…")

GPIO.cleanup()
print("Bye Bye")
