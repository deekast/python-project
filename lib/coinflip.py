import random

class Coin: 
    def flip_coin(self):
        self.coin_flip_result = random.randint(0, 1)
        if self.coin_flip_result == 0:
            print("Wrong, flip a coin")
            self.entrance()
        else:
            print("Wrong again! Oh well, maybe next time. Starting over...")
            self.start_game()

print('Coin flip game')
start = input('Press enter to flip the coin')
count = 0
heads = 0
tails = 0

while count < 100:
    coin_flip = random.randint(0, 1)
    count += 1
    if coin_flip == 0:
        print('Heads')
        heads += 1
    else:
        print('Tails')
        tails += 1

print(f'Number of heads: {heads}, Number of tails: {tails}')