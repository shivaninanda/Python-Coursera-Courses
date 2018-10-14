# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
numberRange = 100
secretNumber = 0
numberOfGuessesLeft = 0


# helper function to start and restart the game
def new_game():  
    global numberRange
    global secretNumber
    global numberOfGuessesLeft
    
    secretNumber = random.randrange(0, numberRange)
    
    print("")
    print ("The range is from 0 to " + str(numberRange) + ".")

    if numberRange == 100: 	
        numberOfGuessesLeft = 7
        print("You have 7 tries to guess the secret number.")
    elif numberRange == 1000:
        numberOfGuessesLeft = 10
        print("You have 10 tries to guess the secret number.")
    
    print("")
      
# define event handlers for control panel
def range100():
    global numberRange
    numberRange = 100 # button that changes range to range [0,100) and restarts
    new_game() 

def range1000():
    global numberRange
    numberRange = 1000 # button that changes range to range [0,1000) and restarts
    new_game()
    
def user_guess(guess):    
    # main game logic goes here	
    global numberOfGuessesLeft
    global secretNumber 
    global numberRange
    
    winOfGame = False
    
    print ("Your guess was " + str(guess) + ".")
    if guess > numberRange:
        print("Your guess was out of the given range.")
        print("But, we will still take one of your tries away.")
    numberOfGuessesLeft = numberOfGuessesLeft - 1
    if numberOfGuessesLeft == 1:
        print ("You have 1 guess left.")
    else:
        print ("You have " + str(numberOfGuessesLeft) + " guess(es) left!")

    if int(guess) == secretNumber:       
        winOfGame = True
    elif int(guess) > secretNumber and guess < numberRange:
        print("Lower!")
    elif int(guess) < secretNumber and guess < numberRange:
        print("Higher!")              
        
    if winOfGame == True:
        print("")
        print ("Congratulations! You have guessed the correct number!")
        new_game()

    elif numberOfGuessesLeft == 0:
        print("")
        print ("You did not guess within 10 tries. The secret number was " + str(secretNumber) + ".")
        new_game()
    
    print("")
    
# create frame
frame = simplegui.create_frame("Guess The Number - Shivani", 250, 250)

# register event handlers for control elements
frame.add_button("Range [1 to 100)", range100, 200)
frame.add_button("Range [1 to 1000)", range1000, 200)
frame.add_input("Enter a Guess: ", user_guess, 100)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric

