# Rock Paper Scissors
# (based on Alyssa Harris code from python tutorials)
#
# Coding Club 18 Jan 2018
#
# This program takes user choice of R P or S and plays it
# against a random choice of R P S by the computer
# and prints out who wins.
#
# updated on the fly during the session to have two user choices instead of
# playing the computer per the kids' request

import random

def convert_choice_to_char(int_choice):
    """
    converts integer version of choice to a character
    """
    rps_dict = {"R": 0, "P":1, "S": 2}
    for k, v in rps_dict.items():
        if v == int_choice:
            #print("found choice!")
            return k

def convert_choice_to_desc(char_choice):
    """
    converts character choice to long description
    """
    rps_dict = {"R": "Rock", "P":"Paper", "S":"Scissors"}
    return rps_dict[char_choice]

def compare_choice(user_choice, computer_choice):
    """
    compares user and computer choice and returns string of who won
    # Rock beats Scissors (R > S)
    # Paper beats Rock (P > R)
    # Scissors beats Paper (S > P)
    Note: I really dislike this here function
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    if user_choice == "R":
        if computer_choice == "S":
            return "User Wins! Rock beats Scissors!"
        else: # must be Paper
            return "User Loses! Computer wins. Paper covers Rock!"
    elif user_choice == "P":
        if computer_choice == "R":
            return "User Wins! Paper covers Rock!"
        else: # must be Scissors
            return "User Loses! Computer wins. Scissors cut Paper."
    else: # user_choice must be Scissors
        if computer_choice == "P":
            return "User Wins! Scissors cut Paper!"
        else: # must be Rock
            return "User Loses! Computer wins. Rock beats Scissors."
def compare_with_ifs(user_choice, computer_choice):
    """
    Decide who wins with if-elses
    """
    print ("")
    print ("##### Who wins by a set of if-else statements ######")
    #Brute force. Nothing overly clever
    # And lets print out what we have chosen and what the computer chose
    print ("User 1 Choice is: ", convert_choice_to_desc(user_choice))
    #print ("Computer Choice is: ", computer_choice)
    print ("User 2 Choice is: ", convert_choice_to_desc(user2_choice))
    #print("Computer Choice is: ", convert_choice_to_desc(computer_choice))

    # Now to decide who wins
    #print(compare_choice(user_choice, computer_choice))
    print(compare_choice(user_choice, user2_choice))

def main():
    keep_playing = True
    while keep_playing:
        valid_choice = False
        valid2_choice = False
        choices = ["R","P","S"]
        while not valid_choice:
            try:
                user_choice = input("Would you like to play Rock (R), Paper (P), or Scissors (S)? ")
                if user_choice in choices:
                    valid_choice = True
                else:
                    print("Case Matters! Try again!")
            except:
                print("Unknown Error at user input")

        while not valid2_choice:
            try:
                user2_choice = input("User 2, would you like to play Rock (R), Paper (P), or Scissors (S)? ")
                if user2_choice in choices:
                    valid2_choice = True
                else:
                    print("Case Matters! Try again!")
            except:
                print("Unknown Error at user input")

        # generate the computer_choice
        # one way
        # computer_choice = random.randint(0, 2)
        # computer_choice_char = convert_choice_to_char(computer_choice)
        # like this way better, randomly generate index and then use the choices
        # list in order to get the element.
        #computer_choice = choices[random.randint(0,2)]
        """
        Decide who wins with if-elses
        """
        print ("")
        print ("##### Who wins by a set of if-else statements ######")
        #Brute force. Nothing overly clever
        # And lets print out what we have chosen and what the computer chose
        print ("User Choice is: ", convert_choice_to_desc(user_choice))
        #print ("Computer Choice is: ", computer_choice)
        print("User 2 Choice is: ", convert_choice_to_desc(user2_choice))

        # Now to decide who wins
        #print(compare_choice(user_choice, computer_choice))
        if user_choice == user2_choice:
            return "It's a tie!"
        if user_choice == "R":
            if user2_choice == "S":
                print( "User 1 Wins! Rock beats Scissors!")
            else: # must be Paper
                return "User 1 Loses! User 2 wins. Paper covers Rock!"
        elif user_choice == "P":
            if user2_choice == "R":
                print(  "User 1 Wins! Paper covers Rock!")
            else: # must be Scissors
                print(  "User 1 Loses! User 2 wins. Scissors cut Paper.")
        else: # user_choice must be Scissors
            if user2_choice == "P":
                print(  "User 1 Wins! Scissors cut Paper!")
            else: # must be Rock
                print(  "User 1 Loses! User 2 wins. Rock beats Scissors.")


        keep_playing = False #stop playing. TODO add choice

#then call it!
main()
