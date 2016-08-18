import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

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
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = [] # Initialize the Hand object to have an empty list of Card objects.

    def __str__(self):
        handstr = ''
        for x in self.hand:
            handstr = handstr + str(x)
        return handstr

    def add_card(self, card):
        self.hand.append(card)

    
    def get_value(self): # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        handvalue = 0
        aces = 0
        for x in self.hand:
            if x.get_rank() == 'A':
                aces += 1
            handvalue += VALUES.get(x.get_rank())
        if aces > 0 and (handvalue + 10) <= 21:
            handvalue += 10
        return handvalue
    
    def draw(self, canvas, p):
        for z in self.hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(z.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(z.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [p[0] + CARD_CENTER[0] + 73 * self.hand.index(z), p[1] + CARD_CENTER[1]], CARD_SIZE)
 
        
# define deck class
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS] # Modeling a deck of cards as list of cards. 
        # shuffle right after initialization
        self.shuffle()

    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.card = self.deck[0]
        self.deck.remove(self.card)
        return self.card


#define event handlers for buttons

def deal(): # Button that shuffles the deck and deals the two cards to both the dealer and the player.
    global outcome, score, in_play, player_hand, dealer_hand, my_deck
    if in_play:
        score -= 1
    player_hand = Hand() # Create new player and dealer hands (stored as global variables)
    dealer_hand = Hand()
    my_deck = Deck()
    my_deck.shuffle() # Shuffle the deck (stored as a global variable)
    player_hand.add_card(my_deck.deal_card()) # Add two cards to each hand.
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    outcome = 'Hit or stand?'
    in_play = True

def hit(): #  If the value of the hand is less than or equal to 21, clicking this button adds an extra card to player's hand. If the value exceeds 21 after being hit, print "You have busted".
    global outcome, score, in_play
    player_hand.add_card(my_deck.deal_card())
    # if busted, assign an message to outcome, update in_play and score
    if player_hand.get_value() > 21:
        outcome = "You have busted. New deal?"
        score -= 1
        in_play = False
        return score, outcome, in_play
    else: # if the hand is in play, hit the player
        outcome = "Hit or stand?"
      
def stand(): # If the player has busted, remind the player that they have busted. Otherwise, repeatedly hit the dealer until his hand has value 17 or more (using a while loop). 
    global outcome, score, in_play
    in_play = False
    if player_hand.get_value() > 21:
        outcome = "You have busted. New deal?"
        score -= 1
        return score, outcome, in_play
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
        else:
            if dealer_hand.get_value() > 21: # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
                outcome = "Dealer busts, you win. New deal?"
                score += 1
                return score, outcome, in_play
            elif dealer_hand.get_value() >= player_hand.get_value(): # The dealer wins ties in this version.
                outcome = "Dealer wins. New deal?"
                score -= 1
                return score, outcome, in_play
            else:
                outcome = "You win. New deal?"
                score += 1
                return score, outcome, in_play
               

# draw handler    
def draw(canvas):
# Drawing a hand as a horizontal sequence of cards where the parameter pos is the position of the upper left corner of the leftmost card.
    dealer_hand.draw(canvas, [150, 100])    
    player_hand.draw(canvas, [150, 370])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [150 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_SIZE)    
    canvas.draw_text(outcome,[50,75],25,"Black")
    canvas.draw_text("Score: "+str(score),[400,50],20,"Black")
    canvas.draw_text("BlackJack",[150,290],50,"Black")
    canvas.draw_text('Current value of your cards: ',[300, 360], 15, "Black")
    canvas.draw_text(str(player_hand.get_value()),[475, 360], 15, "Black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 500, 500)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()
# get things rolling
frame.start()
