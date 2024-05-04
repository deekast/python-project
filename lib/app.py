import random

class App:

    def __init__(self):
        self.user_input = ''
        

    
    def run(self):
        print("Hello, and welcome to Magical Code Quest, a text-based game where you about coding -- and might die!")
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
            

    def start_game(self):
        print("""
              The year is 2024. The world is falling apart, the job market is a mess, and you are living by yourself 
              in a one-bedroom hovel in the magical land of Eboracum Novum with four roommates, all of whom are monstrous
              trolls (literal monstrous trolls -- no looks-shaming here!)-- and your rent is still more than you can afford! 
              """)
        print("""
              Hoping to create a better life for yourself -- and perhaps find a home free of trolls -- you decide to embark on a 
              new career wielding magic -- in other words, you've signed up for Schola FlatFerrum, a coding bootcamp! You've scrounged together the 
              neccesary doubloons (adding a fifth troll roommate to make up for the cost) and you're all ready to go --
              all they need is your name.
              """)
        self.user_input = input(">>> ")
        self.name = self.user_input

        print (f"""Welcome to coding bootcamp, {self.name}! As it turns out, your old rival from childhood is also enrolled at this bootcamp.
               Err... What's their name again?""" )
        
        self.user_input = input(">>> ")
        self.rival = self.user_input

        print(f"That's right, it's {self.rival}! Seems likely you'll see them again at some point. In any event, come on in to bootcamp and get started learning!")
        self.entrance()

    def entrance(self):
        print ("""
               As you enter your coding bootcamp, it becomes clear that something isn't right. A dark aura seems to to coat the room like a thick layer of fog.
               Most of the lights are dimmed, but you see a flicker of light coming from one room. You walk over and investigate.
               """)
        self.first_encounter()

    def first_encounter(self):
        self.question1_input = ""
        self.question2_input = ""

        print("""
              You walk into the room, which has a bloody sign reading "TURING" overhead. The room sits empty except for a single behoodied
              man sitting at  table. Behind his fashionable spectacles, there is nothing behind his glazed-over eyes. He speaks in a ghastly monotone
              """)
        print(f"""Hello, {self.name} I am Chett, an instructor here at Schola FlatFerrum. To move on to the next room -- in our school that is,
              for some reason, set like a railroad apartment -- you must answer a question about Python. If you fail, you'll get a chance to redeem yourself
              with a game of chance""")
        print("""
              Here is your first question:
              True or false: Raccoons are very cute.
              1. True
              2. False
              """)
        while self.question1_input not in ["1", "2"]:
            self.question1_input = input(">>> ")
            if self.question1_input not in ["1", "2"]:
                print("That is not a valid option. Are you sure you want to be a programmer?")
            if self.question1_input == "1":
                print("""
                      That is correct! However, that was a pretty easy question, so I'm not going to count it. Here is your real first question:
                      What does the print() function do in Python?
                      1) It defines a class
                      2) It displays output on the screen 
                      3) It imports modules
                      4) It creates a loop
                      """)
                self.question2_input = input(">>> ")
                if self.question2_input not in ["1","2","3","4"]:
                    print("That is not a valid option. Are you sure you want to be a programmer?")
                if self.question2_input in ["1", "3", "4"]:
                    print("""Incorrect! You should spend more time studying python. Before you do that, though, you'll need to win against me in a 
                          dice roll""")
                    self.dice_game()
                if self.question2_input == "2":
                        print("""That is correct! You may move on to the next room.""")
                        self.second_encounter()
                
            if self.question1_input == "2":
                print("""
                      Bro, this one was supposed to be a gimme. I'm not even gonna let you play a game of chance. So long, sucka!
                      """)
                self.death()

    def dice_game(self):
        print(f"First things first, {self.name} -- you need to roll a die. May lady luck be on your side. And, since I'm feeling generous, let's say tie goes to the challenger. Enter 1 to roll")
        user_roll = random.randint(1,6)
        print(f"You rolled a {user_roll}, {self.name}. Now I'll roll")
        chet_roll = random.randint(1,6)
        if user_roll >= chet_roll:
            print(f"You rolled a {user_roll} and I rolled a {chet_roll}. I guess you win. Good luck in the next room!")
            self.second_encounter()
        if chet_roll > user_roll:
            print(f"I rolled a {chet_roll} and you rolled a {user_roll}. Tough luck, {self.name}. Time to die!")
            self.death()
        
    

    def death(self):
        print("You have died. Will you go to programmer heaven or programmer hell? These are the questions you should ask yourself")

    def second_encounter(self):
        self.question3_input = ''
        print("You go through the door into the next room. Another behoodied man sits in the middle of the room, furiously typing on a laptop.")
        print(f"""Welcome to the Collins Dungeon, {self.name}. I am Sakib, another instructor here at Schola FlatFerrum. As you can tell, things aren't
              exactly going great here. As much as I'd love to just let you go through, you'll need to answer a question about python first. If you don't get it right,
              you'll have a chanve to redeem yourself with a game of chance.
              """)
        print("""Here is your question:
              4. What is a Decorator?
                 1) A function that takes another function as an argument, modifies it, and returns the modified function. 
                 2) A type of function that can only be applied to functions that take exactly two arguments. 
                 3) A way to add new functionality to an existing function without changing its source code. 
                 4) A type of function that can only be applied to functions that do not take any arguments.
              """)
        self.question3_input = input(">>> ")
        if self.question3_input not in ["1","2","3","4"]:
                    print("That is not a valid option. Are you sure you want to be a programmer?")
        if self.question3_input in ["1", "2", "4"]:
                    print("""Incorrect! You should spend more time studying python. Before you do that, though, you'll need to win against me in a 
                          dice roll""")
                    self.coin_flip()
        if self.question3_input == "3":
                        print("""That is correct! You may move on to the next room.""")
                        self.third_encounter()

    def coin_flip(self):
        self.cf_entry=''
        print(f"""
              Sorry, {self.name}, but that is not correct. You REALLY need to brush up on your python. For now, though, we're going to 
              flip a coin to see if you get to move on or, us die.
              """)
        print("Call it in the air:")
        print("Enter 1 for heads or 2 for tails")
        self.cf_entry = input(">>> ")
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
            if coin_land != player_call:
                 print(f"Sorry, it's {coin_land}! You lose! And, unfortunately, that means you die")
                 self.death()
        
        

        


       
    

     