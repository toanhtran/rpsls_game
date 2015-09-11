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

def name_to_number(name):
    # convert name to number using if/elif/else
    
    if name == "rock":
        print 0
    elif name == "Spock":
        print 1
    elif name == "paper":
        print 2
    elif name == "lizard":
        print 3
    elif name == "scissors":
        print 4
    else:
        print "Please enter a valid option: rock, Spock,paper,lizard,scissors"
    return name

def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        print "rock"
    elif number == 1:
        print "Spock"
    elif number == 2:
        print "paper"
    elif number == 3:
        print "lizard"
    elif number == 4:
        print "scissors"
    else:
        print "Please enter a valid number between 0-4."
    return number
    
  

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    pass
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


