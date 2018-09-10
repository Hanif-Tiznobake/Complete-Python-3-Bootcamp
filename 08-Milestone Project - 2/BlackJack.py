import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':[11]}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        print("Cards in deck: {}\n".format(len(self.deck)))
        return ("{}\n"*len(self.deck)).format(*self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.insert(0,card)
        if card.rank=="Ace":
            adjust_for_ace(self)
        print("{} added.".format(str(card)))
        
    def value(self):
        self.value=sum([values[x] for x in self.cards])-10*self.aces
        return self.value
    
    def adjust_for_ace(self):
        if self.value>21:
            self.aces+=1
            print("Ace value adjusted.")

def init_chips():
    while True:
        try:
            n=input("How many chips do you wanna start the game with? ")
            n=int(n)
            break
        except:
            print("{} is not an integer.\n".format(n))
    return n

class Chips:
    
    def __init__(self):
        self.total = init_chips()
        self.bet = 0
        
    def win_bet(self):
        self.bet*=2
    
    def lose_bet(self):
        self.bet=0

def take_bet(chips):
    while True:
        try:
            n=input("How much do you wanna bet? ")
            n=int(n)
            if n<=chips.total:
                print("{} chips was bet.\n".format(n))
                break
            else:
                print("Not enough chips.\n")
        except:
            print("{} is not an integer.\n".format(n))

def hit(deck,hand):
    hand.add_card(deck.deal())

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    do_hit="#"
    while not do_hit in ['Y','N']:
        do_hit=input("You wanna Hit? (Y/N)")
    playing=[True, False]['Y','N'].index(do_hit)

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    do_hit="#"
    while not do_hit in ['Y','N']:
        do_hit=input("You wanna Hit? (Y/N)")
    playing=[True, False]['Y','N'].index(do_hit)

def player_busts(player):
    return player.value>21
    
def player_wins():
    return 

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass

while True:
    # Print an opening statement

    
    # Create & shuffle the deck, deal two cards to each player

    
        
    # Set up the Player's chips
    
    
    # Prompt the Player for their bet

    
    # Show cards (but keep one dealer card hidden)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        
        
        # Show cards (but keep one dealer card hidden)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    
        # Show all cards
    
        # Run different winning scenarios
        
    
    # Inform Player of their chips total 
    
    # Ask to play again

        break
