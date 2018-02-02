# Description: Modified blink.py to use a loop and more functions!
#
# Coding Club 25 Jan 2018 and again 1 Feb 2018
#
# Resources:
#  - https://www.quartoknows.com/page/raspberry-pi-blinking-led

import RPi.GPIO as GPIO
from time import sleep

'''
Remarks: number_of_times is an integer
         speed can be a double
'''
def blink_n(LED_GPIO, number_of_times, speed):
    for n in range (0,number_of_times):
        print ("iteration ", n)
        GPIO.output(LED_GPIO, True) ## Turn on GPIO pin
        time.sleep(speed) ## Wait
        GPIO.output(LED_GPIO, False) ## Switch off GPIO pin
        time.sleep(speed) ## Wait
    print "Done" ## When loop is complete, print "Done"
    GPIO.cleanup()


'''
The main guts
Remarks: calls blink_n
'''

LED_GPIO = 4
print("Getting ready...")
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GPIO, GPIO.OUT)
# call number of blinks and the speed
# note we could change to ask for the number from the user!
blink_n(LED_GPIO,4,2)

# iterations = raw_input("Enter the total number of times to blink: ")
# speed = raw_input("Enter the length of each blink in seconds: ")
# blink_n(LED_GPIO, int(iterations),float(speed))
print("Bye Bye")
