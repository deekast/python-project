import random

# functions 

def populate_deck():
    for suit in ("Hearts", "Diamonds","Clubs", "Spades"):
        for rank in range(2, 15):
            deck.append((suit, rank))

def draw_card(player):
    card = deck[0]
    deck.remove(deck[0])
    print (player + "drew the " + printable_card(card))

def printable_card(card):
    if card[0]  < 11: rank = str(card[0])
    if card[0] == 11: rank = "Jack"
    if card[0] == 12: rank = "Queen"
    if card[0] == 13: rank = "King"
    if card[0] == 14: rank = "Ace"
    fullname = rank + " of " + card[1]
    return fullname


# make deck 
deck = []
populate_deck()
#  shuffle deck

random.shuffle(deck)

while True:
    user_card = draw_card("Player one")
    computer_card = draw_card("Computer")
    if user_card[0] > computer_card[0]: winner = "Player One"
    elif user_card[0] < computer_card[0]: winner = "Computer"
    else: winner = "no one"

    print(winner+ "wins!")
    
    break 

#each player  draws card 


#compare cards 

#tie breaker 

# or continue 





