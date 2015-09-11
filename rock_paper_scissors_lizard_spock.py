# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import math
import random

def name_to_number(name):
    # convert name to number using if/elif/else
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Please enter a valid option: rock, Spock,paper,lizard,scissors"
    return name
    
def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Please enter a valid number between 0-4."
    return number


def rpsls(player_choice): 
    player_choice = name_to_number(player_choice)
    computer_num = random.randrange(0,5)
    score = (player_choice - computer_num) % 5
    print "Player chooses", number_to_name (player_choice)
    print "Computer chooses", number_to_name(computer_num)
    if score == 0:
        print "Player and Computer tie!"
    elif (score == 1) or (score == 2) or (score == 3):
        print "Player Wins!"
    else:
        (score == 4) or (score == 5)
        print "Computer Wins!"
    return ""
   

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
