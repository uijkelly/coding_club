# Description: Modified blink.py to use a loop and more functions!
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

'''
Remarks:
 False = light is on
 True = light is off
'''
def set_led(state):
    if state:
        GPIO.output(LED_GPIO, False)
    else:
        GPIO.output(LED_GPIO, True)

'''
Remarks: number_of_times is an integer
         calls set_led
'''
def blink_n(number_of_times):
    for n in range (0,number_of_times):
        set_led(False)
        print("LED is ON")
        sleep(2)

        set_led(True)
        print("LED is OFF")
        sleep(2)

'''
Remarks: does final on, and cleans up the GPIO
'''
def clean_it_up():
    # now do the final on and cleanup.
    set_led(False)
    print("Turning it on finally…")

    GPIO.cleanup()

'''
The main guts
Remarks: calls blink_n
'''
def main():
    # call number of blinks
    # note we could change to ask for the number from the user!
    blink_n(4)
    
    print("Bye Bye")
