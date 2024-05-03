import random 

class App:

    def __init__(self):
        self.user_input = ''

    
    def run(self):
        print("Hello, and welcome to Magical Code Quest, a text-based game where you learn to code -- and might die!")
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
        print("Magical Code Quest is a text-based game created by Alex, Ben and Dan. It is a CLI game created entirely in Python. We hope you enjoy it")
        print("Start a new game?")

        while self.user_input == "":
            self.user_input = input (">>> ")
            if self.user_input == "Yes":
                self.start_game()
            if self.user_input == "yes":
                self.start_game()
            if self.user_input == "YES":
                self.start_game()
            else:
                print("You have no other option here. Enter 'Yes' and embrace your destiny")

    def start_game(self):
        print('''
              The year is 2024. The world is falling apart, the job market is a mess, and you are living by yourself 
              in a one-bedroom hovel in the magical land of Eboracum Novum with four roommates, all of whom are monstrous
              trolls (literal monstrous trolls -- no looks-shaming here!)-- and your rent is still more than you can afford! 
              ''')
        print(''' 
              Hoping to create a better life for yourself -- and perhaps find a home free of trolls -- you decide to embark on a 
              new career wielding magic -- in other words, you've signed up for a coding bootcamp! You've scrounged together the 
              neccesary doubloons (adding a fifth troll roommate to make up for the cost) and you're all ready to go --
              all they need is your name.
              ''')
        self.user_input = input(">>> ")
        name = self.user_input

        print (f"""Welcome to coding bootcamp, {name}! As it turns out, your old rival from childhood is also enrolled at this bootcamp.
               Err... What's their name again?""" )
        
        self.user_input = input(">>> ")
        rival = self.user_input

        print(f"That's right, it's {rival}! Seems likely you'll see them again at some point. In any event, come on in to bootcamp and get started learning!")
        self.entrance()

    def entrance(self):
        print ('''
               As you enter your coding bootcamp, it becomes clear that something isn't right. A dark aura sits in the 
               center of the room, casting a shadow over everything. Suddenly, a figure steps out from the shadows,
               revealing himself to be your instructor, Chett. He looks at you with a stern yet encouraging gaze and says,
               "Before we begin, let's ensure you're ready. What does the print() function do in Python?"
               A) It defines a class
               B) It displays output on the screen
               C) It imports modules
               D) It creates a loop
               ''')
        if self.user_input.lower() == "b":
            print("Correct The print() function in Python is used to display output on the screen.  Now, let's move on to the next question. #--->>> second question goes here<-----")
           
        

app = App()
app.run()
    
    