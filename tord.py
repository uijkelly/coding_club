# uses python 2.7
#
# For class 2/22/2018
#
# students will modify so that they also:
#       - finish truth scenario 2
#       - finish dare scenario 1 and 2
#       - add new scenarios
#       - add some ASCII art for going to jail
#       - add some ASCII art for worm disease death
# if we get ambitious
# pip install pyfiglet
# print figlet_format('missile!', font='starwars')
# http://www.figlet.org/figlet-man.html
# http://www.figlet.org/examples.html


import random
import time

"""
This is the main function. We run it at the very bottom
"""
def main():
    # set up some things we need below.
    truth_scenario = ["Have you ever sung in the shower? (Y)es or (N)o >>",
    "Have you ever pooped your pants? (Y)es or (N)o >> ",
    "Would you rather eat a (C)ow or a (R)hino >> "]

    dare_scenario = ["Eat gum from under the table.", "Lick the bottom of a muddy shoe"]

    # begin the game.
    name = str(raw_input("What is your name? "))

    print "Hi ", name, "!"
    choice = str(raw_input("(T)ruth or (D)are? "))

    # TRUTH
    if choice == "T":
        print "You chose Truth."
        # pick a random truth scenario
        idx = random.randint(0,2)
        random_truth = truth_scenario[idx]
        answer = str(raw_input(random_truth))
        # now, if it was truth scenario 1, singing in the shower
        if idx == 0 :
            if answer == "Y":
                print "You are on the Voice!" # To do, add more here
            elif answer == "N" :
                print "You should try it some time. It's awesome!"
            else:
                print "Bye! That's not a valid answer. Follow directions next time!"
        # if it was truth scenario 2, pooping pants
        elif(idx == 1):
            print "students to fill this in"
            # TO DO: Students will complete this section. our outline is below
            #If (Y)
            #    PRINT "How embarrassing"
            #If (N)
            #    PRINT "You should try it some time. It's awesome!"
            #else:
            #    print "Bye! That's not a valid answer. Follow directions next time!"
        # if it was truth scenario 3, eat cow or rhino?
        elif idx == 2 :
            if answer == "C" :
                print_bart()
            elif answer == "R":
                print "Go to jail, go directly to jail. Do not pass Go. Do not collect $200."
                print_go_to_jail()
            else:
                print "Bye! That's not a valid answer. Follow directions next time!"
        #end if truth

    # DARE
    elif choice == "D":
        print "You chose Dare."
        # pick random dare_scenario
        idx = random.randint(0,1)
        random_dare = dare_scenario[idx]
        print random_dare
        # if dare scenario 1, eat gum
        if idx == 0:
            # pause for 1 second
            time.sleep(1)
            choose_portal = str(raw_input("Hey, there's a portal under here? You want to go in? (Y)es or (N)o >> "))
            # TO DO
            if choose_portal == "Y":
                print "TO DO, what happens in the portal?"
        # dare scenario 2, lick a shoe
        elif idx == 1:
            # these are the things that could happen after we lick a muddy shoe
            shoe_scenario = ["You like dirt and mud so much, it's all you eat now! Enjoy",
            "You have swallowed a worm and get a weird worm disease."]
            shoe_idx = random.randint(0,1)
            random_shoe = shoe_scenario[shoe_idx]
            print random_shoe
            # eat dirt
            if shoe_idx == 0:
                print_dirt()
            elif shoe_idx == 1:
                print_worm_disease()

    # NEITHER
    else:
        print  "Bye!"

"""
This is a helper print function
Notice that when we print \, we have to 'escape' it and add an extra \. because for
python, this is a special character (character meaning one letter, special character
from the key board, not bart simpson. ;P )
"""
def print_bart():
    print "   , ,\\ ,'\\,'\\ ,'\\ ,\\ ,"
    print ",  ;\\/ \\' `'     `   '  /|"
    print "|\\/                      |"
    print ":                        |"
    print ":                        |"
    print " |                       |"
    print " |                       |"
    print " :               -.     _|"
    print " :                \\     `."
    print " |         ________:______\\"
    print " :       ,'o       / o    ;"
    print " :       \       ,'-----./"
    print "  \\_      `--.--'        )         Don't have a cow, man!"
    print " ,` `.              ,---'|"
    print " : `                     |"
    print "  `,-'                   |"
    print "  /      ,---.          ,'"
    print ",-'            `-,------'"
    print "'   `.        ,--'"
    print "        `-.____/"
    print "-hrr-           \\"

"""
another helper print function
"""
def print_go_to_jail() :
    print "Make me print some art!"

"""
another helper print function
"""
def print_dirt() :
    print "Make me print some art!"

"""
another helper print function
"""
def print_worm_disease() :
    print "Make me print some art!"



"""
Now run things!
"""
main()
