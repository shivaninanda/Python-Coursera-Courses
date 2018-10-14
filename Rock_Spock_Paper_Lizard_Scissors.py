# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    if name == "Rock":
        number = 0
    elif name == "Paper":
        number = 2
    elif name == "Scissors":
        number = 4
    elif name == "Lizard":
        number = 3
    elif name == "Spock":
        number = 1
    return number

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    return name

def rpsls(playerNumber): 
    playerNumber = name_to_number(playerNumber)
    computerNumber = random.randint(0,4)
    player = number_to_name(playerNumber)
    computer = number_to_name(computerNumber)
    print ("Player chooses " + player + ".")
    print ("Computer chooses " + computer + ".")
    difference = computerNumber - playerNumber
    if playerNumber == computerNumber:
        print("Tie!")
    elif difference == 1 or difference == 2 or difference == -3 or difference == -4:
        print("Computer wins!")
    elif difference == 3 or difference == 4 or difference == -1 or difference == -2:
        print("Player wins!")
    print("\n")
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("Rock")
rpsls("Spock")
rpsls("Paper")
rpsls("Lizard")
rpsls("Scissors")

# always remember to check your completed program against the grading rubric
