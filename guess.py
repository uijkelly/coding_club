# uses python 2.7
#
# For class 2/8/2018
#
# students will modify so that they also:
#     - print if the guess is too low or too high
#     - keep track of how many guesses it took and print that also when the guess is right.


#!/usr/bin/python

import random

# keep track of if we are right or not so we know when to stop asking.
youAreRight = False

#pick a random number beween 1 and 10 and saves it into the variable num
num = random.randint(1, 10)

print "I'm thinking of an number between 1 and 10. Guess it!"

#keep asking the user to guess until they get it right.
while not youAreRight:
	#this asks the user their guess and then saves it as an integer into the variable theGuess
	theGuess = int(raw_input("Your guess: "))

	#check if they are right
	if theGuess == num:
		print "Great Job!"
		youAreRight = True   # set to True so that we stop looping/asking to guess.
	else:
		print "Try Again."
