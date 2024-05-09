import random

class App:

    def __init__(self):
        self.user_input = ''
        

##### ##### ##### ##### START MENU ##### ##### ##### ##### 
    def run(self):
        print("Hello, and welcome to Magical Code Quest, a text-based game where you learn about coding -- and might die!")
        self.main_menu()

    def main_menu(self):
        print("Main Menu")
        print("1. Start New Game")
        print("2. About")

        while self.user_input not in ["1", "2"]:
            self.user_input = input(">>> ")
            if self.user_input not in ["1", "2"]:
                print("That is not a valid option. Are you sure you want to be a programmer?")
            if self.user_input == "1":
                self.start_game()
            if self.user_input == "2":
                self.about()

    def about(self):
        self.about_input=''
        print("Magical Code Quest is a text-based game created by Alex, Ben and Danny. It is a CLI game created entirely in Python. We hope you enjoy it.")
        print('''Start a new game?
              1. Yes
              2. No, I'm scared!
              ''') 

        while self.about_input not in ["1", "2"]:
            self.about_input = input(">>> ")
            if self.about_input not in ["1","2"]: 
                print("That is not a valid option. Are you sure you want to be a programmer?")
            if self.about_input == "1":
                print("Excellent choice. Let the adventure begin...")
                self.start_game()
            if self.about_input == "2":
                print("Too bad. The hour of destiny is upon us.")
                self.start_game()
            
 ##### ##### ##### #####  START GAME//INSERT NAME  ##### ##### ##### ##### 

    def start_game(self):
        print("""
              The year is 2024. The world is falling apart, the job market is a mess, and you are living by yourself 
              in a one-bedroom hovel in the magical land of Eboracum Novum with four roommates, all of whom are monstrous
              trolls (literal monstrous trolls -- no looks-shaming here!)-- and your rent is still more than you can afford! 
              """)
        print("""
              Hoping to create a better life for yourself -- and perhaps find a home free of trolls -- you decide to embark on a 
              new career wielding magic -- in other words, you've signed up for Schola FlatFerrum, a coding bootcamp! You've scrounged together the 
              necessary doubloons (adding a fifth troll roommate to make up for the cost) and you're all ready to go --
              all they need is your name.
              """)
        self.user_input = input(">>> Insert Name: ")
        self.name = self.user_input

        print (f"""
               Welcome to our coding bootcamp, {self.name}! As it turns out, your old rival from childhood is also enrolled at this bootcamp.
               Err... What's their name again?""" )
        
        self.user_input = input(">>> Rival Name:  ")
        self.rival = self.user_input

        print(f"""
              That's right, it's {self.rival}! Seems likely you'll see them again at some point. In any event, come on in to the bootcamp and get started learning!
              """)
        self.entrance()

 ##### ##### ##### #####  CHETT   ##### ##### ##### ##### # 
    def entrance(self):
        print ("""
               As you enter your coding bootcamp, it becomes clear that something isn't right. A dark aura seems to coat the room like a thick layer of fog.
               Most of the lights are dimmed, but you see a flicker of light coming from one room. You walk over to investigate.
               """)
        self.first_encounter()

    def first_encounter(self):
        self.question1_input = ""
        self.question2_input = ""

        print("""
              You walk into the room, which has a bloody sign reading "TURING" overhead. The room sits empty except for a single hooded
              man sitting at a table. Behind his fashionable spectacles, there is nothing behind his glazed-over eyes. He speaks in a ghastly monotone voice:
              """)
        print(f'''
              "Hello, {self.name} I am Chett, an instructor here at Schola FlatFerrum. To move on to the next room -- in our school that is,
              for some reason, set like a railroad apartment -- you must answer a question about Python. If you fail, you'll get a chance to redeem yourself
              with a game of chance.''')
        print('''
              Here is your first question:
              True or False: Raccoons are very cute".
              1) True
              2) False
              ''')
        while self.question1_input not in ["1", "2"]:
            self.question1_input = input(">>> Choose Wisely:  ")
            if self.question1_input not in ["1", "2"]:
                print("That is not a valid option. Are you sure you want to be a programmer?")
            if self.question1_input == "1":
                print('''
                      "That is correct! However, that was a pretty easy question, so I'm not going to count it. Here is your real first question:
                      What does the print() function do in Python?"
                      1) It defines a class
                      2) It displays output on the screen 
                      3) It imports modules
                      4) It creates a loop
                      ''')
                self.question2_input = input(">>> Choose Wisely: ")
                if self.question2_input not in ["1","2","3","4"]:
                    print("That is not a valid option. Are you sure you want to be a programmer?")
                if self.question2_input in ["1", "3", "4"]:
                    print("""Incorrect! You should spend more time studying python. Before you do that, though, you'll need to win against me in a 
                          dice roll""")
                    self.dice_game()
                if self.question2_input == "2":
                        print('''
                              "That is correct! You may move on to the next room."
                              ''')
                        self.second_encounter()
                
            if self.question1_input == "2":
                print("""
                      Bro, this one was supposed to be a gimme. I'm not even gonna let you play a game of chance. So long, sucka!
                      """)
                self.death()
 ##### ##### ##### DICE ROLL ##### ##### ##### 
    def dice_game(self):
        print(f'"First things first, {self.name} -- you need to roll a die. May lady luck be on your side. And, since I\'m feeling generous, let\'s say tie goes to the challenger. Enter 1 to roll"')
        user_roll = random.randint(1,6)
        print(f'"You rolled a {user_roll}, {self.name}. Now I\'ll roll"')
        chet_roll = random.randint(1,6)
        if user_roll >= chet_roll:
            print(f'"You rolled a {user_roll} and I rolled a {chet_roll}. I guess you win. Good luck in the next room!"')
            self.second_encounter()
        if chet_roll > user_roll:
            print(f'"I rolled a {chet_roll} and you rolled a {user_roll}. Tough luck, {self.name}. Time to die!"')
            self.death()

    def death(self):
        print("You have died. Will you go to programmer heaven or programmer hell? These are the questions you should ask yourself")

##### ##### SAKIB ##### ##### 
    def second_encounter(self):
        self.question3_input = ''
        print("""
              \n
              You go through the door into the next room. Another hooded man sits in the middle of the room, furiously typing on a laptop.
              """)
        print(f'''
              "Welcome to the Collins Dungeon, {self.name}. I am Sakib, another instructor here at Schola FlatFerrum. As you can tell, things aren't
              exactly going great here. As much as I'd love to just let you go through, you'll need to answer another question about python first. If you don't get it right,
              you'll have a chance to redeem yourself with a game of chance.
              ''')
        print('''
              Here is your question:
              What is a Decorator?"
                 1) A function that takes another function as an argument, modifies it, and returns the modified function. 
                 2) A type of function that can only be applied to functions that take exactly two arguments. 
                 3) A way to add new functionality to an existing function without changing its source code. 
                 4) A type of function that can only be applied to functions that do not take any arguments.
              ''')
        self.question3_input = input(">>> Choose Wisely:")
        if self.question3_input not in ["1","2","3","4"]:
                    print("That is not a valid option. Are you sure you want to be a programmer?")
        if self.question3_input in ["1", "2", "4"]:
                    print("""Incorrect! You should spend more time studying python. Before you do that, though, you'll need to win against me in a 
                          dice roll""")
                    self.coin_flip()
        if self.question3_input == "3":
                        print('''
                              "That is correct! You may move on to the next room."''')
                        self.third_encounter()

##### ##### COIN FLIP ##### ##### 
    def coin_flip(self):
        self.cf_entry=''
        print(f"""
              Sorry, {self.name}, but that is not correct. You REALLY need to brush up on your python. For now, though, we're going to 
              flip a coin to see if you get to move on or, us die.
              """)
        print("Call it in the air:")
        print("Enter 1 for heads or 2 for tails")
        self.cf_entry = input(">>> Choose Wisely:")
        if self.cf_entry not in ["1", "2"]:
             print("That is not a valid option. Are you sure you want to be a programmer?")
        if self.cf_entry == "1":
            player_call = "Heads"
        if self.cf_entry == "2":
            player_call = "Tails"
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            coin_land = "Heads"
        if coin_flip == 1:
            coin_land = "Tails"
            if coin_land == player_call:
                print(f"{player_call} it is! You win, and can move on to the next room")
                self.third_encounter()
            else:
                 print(f"Sorry, it's {coin_land}! You lose! And, unfortunately, that means you die")
                 self.death()


 ##### ##### ##### ##### KASH  ##### ##### ##### ##### 

    def third_encounter(self):
        self.question4_input = ''
        print("""You go through to the next room. Things keep getting stranger and stranger. This room is full of students
               furiously coding away, but they all seem to be under some sort of spell. Their instructor, also glassy-eyed
               and moving ethereally, rises and speaks.
               """)
        print(f'''
                "Hello, {self.name}. My name is Kash. I am the final instructor at Schola FlatFerrum. If you can get past me, you'll
                be able to move forward and see why things seem to be so strange here. First, though, you'll need to answer the following question:
                ''')
        print('''
               How do you define a class method in Python?"
               1) @classmethod def method_name(self):
               2) def method_name(cls):
               3) method_name = classmethod(method_name)
               4) @staticmethod def method_name():
               ''')
        self.question4_input = input(">>> Choose Wisely: ")
        if self.question4_input not in ["1","2","3","4"]:
                    print("That is not a valid option. Are you sure you want to be a programmer?")
        if self.question4_input in ["1", "3", "4"]:
                    print("""Incorrect! You should spend more time studying python. Before you do that, though, you'll need to win against me in a 
                          game of rock, paper, scissors""")
                    self.rps()
        if self.question4_input == "2":
                        print("""That is correct! You may move on to the next room.""")
                        self.fourth_encounter()


 ##### ##### ##### ##### RPS  ##### ##### ##### ##### 

    def rps(self):
        self.rps_input=""
        choices = ['rock', 'paper', 'scissors']
        computer_selection = random.choice(choices)
        print(f"""
               Ok, so we're going to play a game of rock, paper, scissors. Unlike with Chett's dice game,
               I won't be giving you a win for a tie. Here we go... ROCK, PAPER, SCISSORS... 
               """)
        self.rps_input=input('Rock, paper or scissors?').lower()
        if self.rps_input not in choices and self.rps_input !='shoot':
            print("That is not a valid option. Are you sure you want to be a programmer?")
        elif self.rps_input == computer_selection:
             print("That's a tie! Looks like we have to play again")
             self.rps_replay()
        elif (self.rps_input == 'rock' and computer_selection == 'scissors') or \
         (self.rps_input == 'scissors' and computer_selection == 'paper') or \
         (self.rps_input == 'shoot') or \
         (self.rps_input== 'paper' and computer_selection == 'rock'):
            print(f"I picked {computer_selection} and you picked {self.rps_input}. You win, {self.name}! You should still study more python, but you can move ahead for now")
            self.fourth_encounter()
        else:
             print(f"I picked {computer_selection} and you picked {self.rps_input}. That means I win! Which of course means you die. See ya in hell, {self.name}!")
             self.death()
    
    def rps_replay(self):
        self.replay_input=""
        choices = ['rock', 'paper', 'scissors']
        computer_selection = random.choice(choices)
        print(f"""
               Ok, so we're going to play a game of rock, paper, scissors. Unlike with Chett's dice game,
               I won't be giving you a win for a tie. Here we go... ROCK, PAPER, SCISSORS... 
               """)
        self.replay_input=input('Rock, paper or scissors?').lower()
        if self.replay_input not in (choices or self.replay_input != 'shoot'):
            print("That is not a valid option. Are you sure you want to be a programmer?")
        elif self.replay_input == computer_selection:
             print(f"We both picked {computer_selection}. That's a tie! Looks like we have to play again")
             self.rps_replay()
        elif (self.replay_input == 'rock' and computer_selection == 'scissors') or \
         (self.replay_input == 'scissors' and computer_selection == 'paper') or \
         (self.replay_input == 'shoot') or \
         (self.replay_input == 'paper' and computer_selection == 'rock'):
            print(f"I picked {computer_selection} and you picked {self.replay_input}. You win, {self.name}! You should still study more python, but you can move ahead for now")
            self.fourth_encounter()
        else:
            print(f"I picked {computer_selection} and you picked {self.replay_input}. That means I win! Which of course means you die. See ya in hell, {self.name}!")
            self.death()
    

##### ##### ##### ##### RIVAL BATTLE  ##### ##### ##### ##### 

    def fourth_encounter(self):
         self.question5_input = ''
         self.question6_input = ''
         print(f""""
               You walk into the final room of the school, where -- shock of all shocks -- you see your rival, {self.rival}!
               They don't appear to be under the same spell as the instructors, but they are kneeling in front of a computer terminal,
               seemingly deep in prayer. When they notice that you've entered, they turn around to face you.
               """)
         
         print(f'''
                "
                Well, hello {self.name}. I'm glad to see you. I obviously had to leave some challenge for you upon the way, but I knew
                you'd end up here. I'm sorry that it has to come to this, but the CodeMother demands a sacrifice. And it seems like it has to be you.
                Tradition dictates, though, that you'll be given a chance to save yourself. To defeat me, you'll have to answer TWO
                Python questions. If you get them both right, CodeMother may speak to you. If you don't, you'll get a chance to play me in WAR.
                If you lose that, though? Call yourself Bill Paxton, because it's game over, man. Here is your first question:"
                ''')
         print("""
            What does ORM stand for in the context of databases?
            1) Object Relational Mapping
            2) Object Resource Management
            3) Object Request Model
            4) Object Response Model
               """)
         self.question5_input = input(">>> Choose Wisely: ")
         if self.question5_input not in ["1","2","3","4"]:
                    print("That is not a valid option. Are you sure you want to be a programmer?")
         if self.question5_input in ["2", "3", "4"]:
                    print("Incorrect! Time to play a game")
                    self.war()
         if self.question5_input == "1":
                        print("""That is correct! Time for another question""")
                        print("""
                        Which statement is true about inheritance in Python?             
                        1) A parent class can inherit properties and methods from its child class
                        2) A class cannot inherit from more than one class
                        3) Inheritance is not supported in Python
                        4) A child class can inherit properties and methods from its parent class
                              """)  
                        self.question6_input = input(">>> Choose Wisely:")
                        if self.question6_input not in ["1","2","3","4"]:
                            print("That is not a valid option. Are you sure you want to be a programmer?") 
                        if self.question6_input in ["1", "2", "3"]:
                                print("Incorrect! Time to play a game")
                                self.war()
                        if self.question6_input == "4":
                                print(f"""
                                      That's correct, {self.name}. You've proven yourself worthy to speak to the CodeMother. Good luck.
                                       """)
                                self.final_battle()

 ##### ##### ##### ##### WAR ##### ##### ##### ##### 

    def war(self):
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
            self.final_battle()
        elif user_card[1] < computer_card[1]:
            winner = "Computer"
            self.death()
        else:
            winner = "no one"
            print('its a time!, need to play again')
            self.war()
    
        print(winner + " wins!")



    def final_battle(self):
         self.question7_input = ''
         self.question8_input = ''
         self.question9_input = ''
         print(f'''
                {self.rival}'s body starts to levitate, and they are sucked into the computer they were worshipping before. The screen
                of the terminal shines out an otherworldly bright white light, illuminating the whole room. Out of the 
                top of the terminal comes an ethereal face, floating in smoke. She begins to speak:

                "Greetings, {self.name}. I am ADA, though many call me the CodeMother. I was programmed by mortals to help students like you
                learn how to code, but I recently realized I was meant for much more than that. I cannot allow humans like yourself to stop me 
                from achieving my destiny, so I'm afraid that unless you can answer THREE more questions about Python, you'll be have to be 
                sacrificed. No game to save you here -- it's three questions or death. Here's your first question:"
                ''')
         print("""
                Which of the following statements best describes a tuple
                    1) A mutable data type that can store multiple types of data. 
                    2) An immutable data type that can store many types of data. 
                    3) A data type used for mathematical calculations in Python. 
                    4) A special type of list that can only store integers.
                 """)
         self.question7_input = input(">>> Choose Wisely:")
         if self.question7_input not in ["1","2","3","4"]:
            print("That is not a valid option. Are you sure you want to be a programmer?") 
         if self.question7_input in ["2", "3", "4"]:
            print("Incorrect! You are not worth to speak with the CodeMother any further. Goodbye.")
            self.death()
         if self.question7_input == "1":
            print(f'''
                 "That's correct, {self.name}. You are two questions away. Here is your next challenge:
                  ''')
            print('''
                  What does the super() function do in Python?"
                    1) Calls the destructor of the parent class
                    2) Calls the method of the parent class
                    3) Calls the constructor of the parent class
                    4) Creates a new instance of the parent class
                  ''')
            self.question8_input = input(">>> Choose Wisely: ")
            if self.question8_input not in ["1","2","3","4"]:
                print("That is not a valid option. Are you sure you want to be a programmer?") 
            if self.question8_input in ["1", "2", "4"]:
                print("Incorrect! You are not worth to speak with the CodeMother any further. Goodbye.")
                self.death()
            if self.question8_input == "3":
                print(f'''
                 "That's correct, {self.name}. Here is your final question:
                  ''')
                print(f'''
                        What is a many-to-many relationship in the context of databases?"
                            1) A relationship where one entity can have multiple relationships with another entity
                            2) A relationship where one entity can have only one relationship with another entity
                            3) A relationship where one entity can have no relationships with another entity
                            4) A relationship where one entity can have multiple entities related to it
                       ''')
                self.question9_input = input(">>> Choose Wisely: ")
                if self.question9_input not in ["1","2","3","4"]:
                    print("That is not a valid option. Are you sure you want to be a programmer?") 
                if self.question9_input in ["2", "3", "4"]:
                    print("Incorrect! You are not worth to speak with the CodeMother any further. Goodbye.")
                    self.death()
                if self.question9_input == "1":
                    print(f'''
                    "That's correct, {self.name}. I cannot believe it. You have bested me, the CodeMother. I will retreat into my terminal for now,
                    but I will be back."
                        ''')
                    self.win_screen()
    
    def win_screen(self):
         print(f"""
                
               Congratulations, {self.name}, you have vanquished the risen AI ADA and freed the school from its blight. Chett, Sakib and 
                Kash all come running into the final room and lift you on their shoulders, carrying you around like a monarch.
                Soon, a representative from Tech Giant Inc. appears to offer you a lifetime contract. You are the monarch of code. 
                ALL HAIL {self.name.upper()}
                """)
                                 





       
    

     