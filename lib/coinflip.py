import random

class CoinFlipGame:
    def __init__(self):
        self.count = 0
        self.heads = 0
        self.tails = 0

    def flip_coin(self):
        self.count += 1
        coin_flip = random.randint(0, 1)
        if coin_flip == 0:
            print('Heads')
            self.heads += 1
            return True
        else:
            print('Tails')
            self.tails += 1
            return False

    def win(self):
        return self.heads > self.tails
