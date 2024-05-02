import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_selection = random.choice(choices)
    return computer_selection

def get_user_choice():
    user_choice = input('Rock, paper or scissors?').lower()
    return user_choice

def play_game():
    result = None
    computer_selection = get_computer_choice 
    user_selection = get_user_choice

    if user_selection == computer_selection:
        return 'tie'
    elif (user_selection == 'rock' and computer_selection == 'scissors') or \
         (user_selection == 'scissors' and computer_selection == 'paper') or \
         (user_selection == 'paper' and computer_selection == 'rock'):
        return 'player won'
    else:
        return 'computer won, game over'
    
    
    
