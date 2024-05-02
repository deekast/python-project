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
            self.user_input = input(">>> ").lower()
            if self.user_input == "yes":
                self.start_game()
            else:
                print("You have no other option here. Enter 'Yes' and embrace your destiny")


    def start_game(self):
        pass
