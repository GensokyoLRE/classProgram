"""
Program: classProg0.py
Author: Phillip "Hifumi" Cuesta
Last Mod: 1932 PST 10/25/18
Purpose:
HW program to work with classes.
In this instance, a simplistic FFTCG match calculator with time spent (like a chess clock).


"""
import webbrowser
import time


class Player:
    """Class to """
    _count = 0

    def __init__(self, name='Basic Bob', deck='Mono Bland'):
        self.name = name
        self.deck = deck
        self.game_set = []
        x = 0
        while x < 3:
            self.game_set.append("Game %i:\n"
                                 "%s **7** to **7** (vs. InsertPlayer)" % (x+1, self.name))
            x += 1
        Player._count += 1

    def getName(self):
        return self.name

    def getDeck(self):
        return self.deck

    def changeDeck(self, deck):
        self.deck = deck

    def getCount(self):
        return Player._count

    def set_game_set(self, pd1, pd2, pl1, pl2):
        if pd1 >= 7:
            pass  # TBD
        elif pd2 >= 7:
            pass  # TBD
        else:
            return False

    def __str__(self):
        return "Name: " + self.name + "\nDeck: " + self.deck + "\nRecord: "


if __name__ == "__main__":
    print("Now accepting player 1...\n")
    p1 = Player(input("Enter name or press Enter for default name: "),
                input("Enter name of deck or press Enter for default name: "))
    print("Player 1 accepted. Now accepting player 2...\n")
    p2 = Player(input("Enter name or press Enter for default name: "),
                input("Enter name of deck or press Enter for default name: "))
    print("Player 2 accepted. Now loading environment...")
    time.sleep(5)
