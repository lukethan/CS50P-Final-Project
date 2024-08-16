import random
import sys
import os

class Player:

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.amount = 0
        self.number = 0
        self.gamechoice = 0
        self.bet_type = ""

    def r_bet(self):
        while True:
            self.bet_type = input("\nWould you like to bet on 'Red', 'Black', 'Evens', 'Odds', or a 'Number'? ")
            if self.bet_type.lower().strip() == "red":
                self.bet_type = "red"
                break
            elif self.bet_type.lower().strip() == "black":
                self.bet_type = "black"
                break
            elif self.bet_type.lower().strip() == "evens":
                self.bet_type = "even"
                break
            elif self.bet_type.lower().strip() == "odds":
                self.bet_type = "odd"
                break
            elif self.bet_type.lower().strip() == "number":
                self.bet_type = "number"
                break
            else:
                print("\nPlease type in 'Red', 'Black', 'Evens', 'Odds', or a Number'")

    def game(self):
        while True:
            self.gamechoice = input("\nWould you like to play Roulette or Slots today? ")
            if self.gamechoice.lower().strip() == "roulette":
                self.gamechoice = 1
                break
            elif self.gamechoice.lower().strip() == "slots":
                self.gamechoice = 2
                break
            else:
                print("\nPlease type in 'Roulette' or 'Slots'")





    @classmethod
    def get(cls):
        balance = random.randint(10,100)
        while True:
            try:
                name = input("\nWhat is your name? ")
                if name.strip().isalpha():
                    return cls(balance, name)
                else:
                    print("Invalid Name")
            except EOFError:
                pass

    def __str__(self):
        return(f"\nHello {self.name}, you have ${self.balance} available" )

    def bet(self):
        while True:
            try:
                self.amount = int((input("\nHow much would you like to bet? ")))
                if (self.amount) <= self.balance and self.amount > 0:
                    self.balance -= (self.amount)
                    break
                else:
                    print("Insufficient Funds or Invalid Negative Number Entered")
            except ValueError:
                print("\nPlease enter a whole number with no other characters")
                pass

    def get_num(self):
        while True:
            self.number = int(input("Which number would you like to bet on? "))
            if 0 <= self.number <= 38:
                return self.number
            else:
                print("Please enter a number between 0-38")


    def check(self, winnings):
        self.balance += winnings
        if winnings == 0 and self.balance == 0:
            os.system('clear')
            sys.exit(f"\n\n\n\n\n⚠️  GAME OVER ⚠️\n\n\nUH OH {self.name}, you lost it ALL!\n\n\n⚠️  GAME OVER ⚠️\n\n\n")
        print(f"\nYou now have ${self.balance} available\n(Enter Ctrl/Cmd D at any point to exit)")

