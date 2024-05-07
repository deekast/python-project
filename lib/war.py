import random

# Functions
def populate_deck(deck):
    for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
        for rank in range(2, 15):
            deck.append((suit, rank))

def draw_card(player):
    card = deck[0]
    deck.remove(deck[0])
    print(player + " drew the " + printable_card(card))
    return card

def printable_card(card):
    if card[1] < 11:
        rank = str(card[1])
    elif card[1] == 11:
        rank = "Jack"
    elif card[1] == 12:
        rank = "Queen"
    elif card[1] == 13:
        rank = "King"
    elif card[1] == 14:
        rank = "Ace"
    fullname = rank + " of " + card[0]
    return fullname

# Make deck
deck = []
populate_deck(deck)
# Shuffle deck
random.shuffle(deck)

# Play one round
user_card = draw_card("Player one")
computer_card = draw_card("Computer")
if user_card[1] > computer_card[1]:
    winner = "Player One"
elif user_card[1] < computer_card[1]:
    winner = "Computer"
else:
    winner = "no one"
print(winner + " wins!")
