"""
Program: PoemClasses.py
Author: Phillip "Hifumi" Cuesta
Last Mod: 8:14 PM 10/30/18
Purpose: Read in a file that contains some form of poetry to a
class and see if it's a haiku.
"""
import os


class Poem:
    """Read in and print the poem, as well as evaluate for haiku."""
    _count = 0

    def __init__(self, file):
        self.lines = file
        Poem._count += 1

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def get_count(self):
        return self._count

    def is_haiku(self, file):
        print("Checking for a haiku possibility...\n")
        lines = file.splitlines()
        lines.pop(0)
        count = 0
        is_hai = False
        for line in lines:
            print(line)
            count += 1
        if count == 3:
            is_hai = True
        if is_hai:
            print("\nIt may be a haiku. Running in-testing evaluation of syllables...")
            syll = lambda x: len(''.join(" x"[c in "aeiouy"] for c in (x[:-1] if 'e' == x[-1] else x)).split())
            h_check = []
            for line in lines:
                h_check.append(syll(line.lower()))
            if h_check == [5, 7, 5]:
                print("\nT'was a haiku.")
                return True
            else:
                print("\nT'waint. Nice poem though.")
                print(h_check)
                return False
        else:
            print("\nIt's not a haiku. Still nice.")
            return False


while True:
    try:
        openFile = input("Enter a poem file name: ") + ".txt"
        if not os.path.isfile(openFile):
            openFile = "DefaultPoem.txt"
            print("Defaulting to DefaultPoem\n")
        fullFile = open(openFile, 'r').read()
        poemType = Poem(fullFile)
        poemLines = fullFile.splitlines()
        aName, aAuthor = poemLines[0].split(" by ")
        poemType.set_name(aName)
        poemType.set_author(aAuthor)
        print("Name: %s\n"
              "Author: %s\n"
              "Poem:\n" % (poemType.get_name(), poemType.get_author()))
        poemType.is_haiku(fullFile)
        cont = input("Do you wanna do another one? Y/N: ")
        if cont.upper() == "N":
            print("You checked %i poems. Thank you for using this program!" % poemType.get_count())
            exit(0)
    except Exception as e:
        print("Error: %s" % e)

