import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards
    global facedUp
    global condition
    global numberOne
    global numberTwo
    global score
    global numberOfTurns
    condition = 0
    score = 0
    numberOfTurns = 0
    numberOne = -1
    numberTwo = -1
    cards = [number for number in range(8)]*2
    random.shuffle(cards)
    facedUp = [False]*16
     
# define event handlers
def mouseclick(pos):
    # add game condition logic here
    global condition
    global score
    global numberOne
    global numberTwo
    global numberOfTurns
    cardPosition = list(pos)[0]//50 
    if not facedUp[cardPosition]:
        if condition == 0:
            numberOne = cardPosition
            facedUp[cardPosition] = True
            condition = 1
        elif condition == 1:
            numberTwo = cardPosition
            facedUp[cardPosition] = True
            if cards[numberOne] == cards[numberTwo]:
                score += 1
            condition = 2
            numberOfTurns += 1
            label.set_text("Turns = " + str(numberOfTurns))
        else:
            if cards[numberOne] != cards[numberTwo]:
                facedUp[numberOne], facedUp[numberTwo] = False, False
                numberOne, numberTwo = -1, -1
            numberOne = cardPosition
            facedUp[cardPosition] = True
            condition = 1   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for eachPass in range(16):
        if facedUp[eachPass]:
            canvas.draw_polygon([[eachPass * 50, 0], [(eachPass + 1) * 50, 0], [(eachPass + 1) * 50, 100], [i * 50, 100]], 1, "Aqua", "Black")
            canvas.draw_text(str(cards[eachPass]), (eachPass * 50 + 11, 69), 55, "Aqua")
        else:
            canvas.draw_polygon([[eachPass * 50, 0], [(eachPass + 1) * 50, 0], [(eachPass + 1) * 50, 100], [eachPass * 50, 100]], 1, "Aqua", "Teal")
    label.set_text("Turns = " + str(numberOfTurns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory - Shivani Nanda", 800, 100)
frame.add_button("RESET", new_game)
label = frame.add_label("Number of Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
