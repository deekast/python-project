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

        while self.main_user_input not in ["1", "2"]:
            self.main_user_input = input(">>> ")
            if self.user_input not in ["1", "2"]:
                print("That is not a valid option. Are you sure you want to be a programmer?")
            if self.main_user_input == "1":
                self.start_game()
            if self.main_user_input == "2":
                self.about()

    def about(self):
        print("Magical Code Quest is a text-based game created by Alex, Ben and Dan. It is a CLI game created entirely in Python. We hope you enjoy it.")
        print('''Start a new game?
              1. Yes
              2. No, I'm scared!
              ''')

        while self.about_user_input not in ["1", "2"]:
            self.about_user_input = input(">>> ")
            print("That is not a valid option. Are you sure you want to be a programmer?")
            if self.about_user_input == "1":
                print("Excellent choice. Let the adventure begin...")
                self.start_game()
            if self.about_user_input == "2":
                print("Too bad. The hour of destiny is upon us.")
                self.start_game()
            

    def start_game(self):
        print('''
              The year is 2024. The world is falling apart, the job market is a mess, and you are living by yourself 
              in a one-bedroom hovel in the magical land of Eboracum Novum with four roommates, all of whom are monstrous
              trolls (literal monstrous trolls -- no looks-shaming here!)-- and your rent is still more than you can afford! 
              ''')
        print(''' 
              Hoping to create a better life for yourself -- and perhaps find a home free of trolls -- you decide to embark on a 
              new career wielding magic -- in other words, you've signed up for Schola FlatFerrum, a coding bootcamp! You've scrounged together the 
              neccesary doubloons (adding a fifth troll roommate to make up for the cost) and you're all ready to go --
              all they need is your name.
              ''')
        self.user_input = input(">>> ")

        self.name = self.user_input

        print (f'''Welcome to coding bootcamp, {self.name}! As it turns out, your old rival from childhood is also enrolled at this bootcamp.
               Err... What's their name again?''' )
        
        self.user_input = input(">>> ")
        self.rival = self.user_input

        print(f"That's right, it's {self.rival}! Seems likely you'll see them again at some point. In any event, come on in to bootcamp and get started learning!")
        self.entrance()

    def entrance(self):

        print ('''
               As you enter your coding bootcamp, it becomes clear that something isn't right. A dark aura seems to to coat the room like a thick layer of fog.
               Most of the lights are dimmed, but you see a flicker of light coming from one room. You walk over and investigate.
               ''')
        self.first_encounter()

    def first_encounter(self):
        print('''
              You walk into the room, which has a bloody sign reading "TURING" overhead. The room sits empty except for a single behoodied
              man sitting at  table. Behind his fashionable spectacles, there is nothing behind his glazed-over eyes. He speaks in a ghastly monotone
              ''')

        print(f'''Hello, {self.name} I am Chett, an instructor here at Schola FlatFerrum. To move on to the next room -- in our school that is,
              for some reason, set like a railroad apartment -- you must answer a question about Python. If you fail, you'll get a chance to redeem yourself

        print(f'''Hello, {start_game.name} I am Chett, an instructor here at Schola FlatFerrum. To move on to the next room -- in our school that is,
              for some reason, set like a railroad apartment, you must answer a question about Python. If you fail, you'll get a chance to redeem yourself

              1. True
              2. False
              ''')
        while self.user_input not in ["1", "2"]:
            self.user_input = input(">>> ")
            if self.user_input not in ["1", "2"]:
                print("That is not a valid option. Are you sure you want to be a programmer?")
            if self.user_input == "1":
                print('''
                      That is correct! However, that was a pretty easy question, so I'm not going to count it. Here is your real first question:
                      What does the print() function do in Python?
                      A) It defines a class
                      B) It displays output on the screen 
                      C) It imports modules
                      D) It creates a loop
                      ''')
                self.user_input = input(">>> ")
                if self.user_input not in []
                
            if self.user_input == "2":
                print('''
                      Bro, this one was supposed to be a gimme. I'm not even gonna let you play a game of chance. So long, sucka!
                      ''')
                self.death()

    

    def death(self):
        print("You have died. Will you go to programmer heaven or programmer hell? These are the questions you should ask yourself")
       
    

              A. True
              B. False
              ''')



     