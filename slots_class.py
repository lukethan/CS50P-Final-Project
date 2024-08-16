import random
import os


class Slot():
    char = ["⭐","🍒","🍀"]
    winchar = ["⭐"] #used for testing purposes to guarantee a win
    losechar = ["🍒"] #used for testing purposes to guarantee a loss
    def __init__(self):
        self.first = 0
        self.second = 0
        self.third = 0
        self.winnings = 0

    def play(self,amount, name):
        self.first = random.choice(self.char)
        self.second = random.choice(self.char)
        self.third = random.choice(self.char)
        os.system('clear')
        print(f"\n\n{self.first}|{self.second}|{self.third}")
        if self.first == self.second == self.third:
            self.winnings = int(amount*5)
            print(f"\nCongrats {name}, YOU JUST WON ${self.winnings}!!!!!")
        else:
            self.winnings = 0
            print("\nBetter luck next time!")

    def testwin(self,amount, name):
        self.first = self.winchar
        self.second = self.winchar
        self.third = self.winchar
        os.system('clear')
        print(f"\n\n{self.first}|{self.second}|{self.third}")
        if self.first == self.second == self.third:
            self.winnings = int(amount*5)
            print(f"\nCongrats {name}, YOU JUST WON ${self.winnings}!!!!!")
        else:
            self.winnings = 0
            print("\nBetter luck next time!")

    def testloss(self,amount, name):
        self.first = self.winchar
        self.second = self.losechar
        self.third = self.winchar
        os.system('clear')
        print(f"\n\n{self.first}|{self.second}|{self.third}")
        if self.first == self.second == self.third:
            self.winnings = int(amount*5)
            print(f"\nCongrats {name}, YOU JUST WON ${self.winnings}!!!!!")
        else:
            self.winnings = 0
            print("\nBetter luck next time!")

