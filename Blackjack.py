# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
duringPlay = False
messageForUser = ""
score = 0
numberOfGame = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
    
    def __str__(self):
        return self.suit + self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def draw(self, canvas, pos):
        cardLocation = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, cardLocation, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    # create Hand object
    def __init__(self):
        self.cards = []
    
    # return a string representation of a hand
    def __str__(self):
        hand = ("Hand contains ")
        
        for card in self.cards:
            hand += str(card) + " "
        
        return hand
    
    # add a card object to a hand
    def add_card(self, card):
        self.cards.append(card)
    
    # compute the value of the hand
    def get_value(self):
        hand_value = 0
        ace = False
        
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace = True
        
        if not ace:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
    
    # draw a hand on the canvas
    def draw(self, canvas, pos):
        cardNumber = 0
        for card in self.cards:
            if pos[1] == 310 and cardNumber == 0 and duringPlay == True:
                # draw card back
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                                  [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]],
                                  CARD_BACK_SIZE)
            else:
                # draw face card
                card.draw(canvas, [pos[0] + (cardNumber % 7) * 77, pos[1] + (cardNumber // 7) * 102])
            cardNumber += 1

# define deck class 
class Deck:
    # create a Deck object
    def __init__(self):
        self.cards = []
        self.cardsPosition = 0
        
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
        
    # add cards back to deck and shuffle
    def shuffle(self):
        self.cardsPosition = 0
        random.shuffle(self.cards)
        
    # deal a card object from the deck
    def deal_card(self):
        self.cardsPosition -= 1
        return self.cards[self.cardsPosition]
    
    # return a string representing the deck
    def __str__(self):
        deck = "Deck contains "
        for card in self.cards:
            deck += str(card) + " "
        return deck

#define event handlers for buttons
def deal():
    global duringPlay, outcome, score, numberOfGame, playersHand, dealersHand
    
    deck.shuffle()
    playersHand.cards = []
    dealersHand.cards = []
    
    numberOfGame += 1
    
    playersHand.add_card(deck.deal_card())
    playersHand.add_card(deck.deal_card())
    dealersHand.add_card(deck.deal_card())
    dealersHand.add_card(deck.deal_card())
    
    if duringPlay:
        score -= 1
        outcome = "You lost the round! New round: Hit or stand?"
    else:
        outcome = "Hit or stand?"
    
    duringPlay = True

def hit():
    global duringPlay, outcome, score, playersHand
    
    if duringPlay:
        playersHand.add_card(deck.deal_card())
        if playersHand.get_value() <= 21:
            outcome = "Hit or stand?"
        else:
            outcome = "You have busted! Press DEAL to play the game again!"
            score -= 1
            duringPlay = False

def stand():
    global duringPlay
    global outcome, score, playersHand, dealersHand
    
    if duringPlay:
        duringPlay = False
        if playersHand.get_value() > 21:
            outcome = ("You have busted! Press DEAL to play the game again!")
            score -= 1
        else:
            while dealersHand.get_value() < 17:
                dealersHand.add_card(deck.deal_card())
            
            if dealersHand.get_value() > 21:
                score += 1
                outcome = ("You won! Press DEAL to play the game again!")
            elif dealersHand.get_value() >= playersHand.get_value():
                score -= 1
                outcome = ("You have busted! Press DEAL to play the game again!")
            else:
                score += 1
                outcome = ("You won! Press DEAL to play the game again!")

# draw handler    
def draw(canvas):
    # draw title
    canvas.draw_text("Blackjack", [180, 45], 30, "Aqua")

    # draw text
    canvas.draw_text("Player", [15, 75], 24, "White")
    canvas.draw_text("Dealer", [15, 225], 24, "White")
    canvas.draw_text("Score: " + str(score), [400, 65], 24, "Green")
    canvas.draw_text("Game # " + str(numberOfGame), [400, 85], 21, "Yellow")
    canvas.draw_text(outcome, [15, 375], 24, "White")

    # draw cards
    playersHand.draw(canvas, [10, 85])
    dealersHand.draw(canvas, [10, 235])

# initialization frame
frame = simplegui.create_frame("Blackjack", 550, 400)
frame.set_canvas_background("Black")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# initializing game
deck = Deck()
playersHand = Hand()
dealersHand = Hand()
deal()

# get things rolling
frame.start()  
