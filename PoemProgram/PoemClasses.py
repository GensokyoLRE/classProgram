"""
Program: PoemClasses.py
Author: Phillip "Hifumi" Cuesta
Last Mod: 8:14 PM 10/30/18 (text modded 9:41 PM 10/31/18 spoopy)
Purpose: Read in a file that contains some form of poetry to a
class and see if it's a haiku.
Disclaimer: Only works if first line format is "NameOfPoem by NameOfAuthor".
"""
import os


class Poem:
    """Read in and print the poem, as well as evaluate for haiku."""
    _count = 0

    def __init__(self, file):
        """
        Intializes Poem class.
        :param file: Takes in the file given to the class and reads to variable.
        """
        self.lines = file
        Poem._count += 1

    def get_name(self):
        """
        Gets name/title of the poem.
        :return: Name of poem.
        """
        return self.name

    def get_author(self):
        """
        Gets author of poem.
        :return: Author of poem.
        """
        return self.author

    def set_name(self, name):
        """
        Lets user enter name of poem.
        :param name: Name of poem.
        :return: Nothing
        """
        self.name = name

    def set_author(self, author):
        """
        Lets user enter author of poem.
        :param author: Author of poem.
        :return: Nothing
        """
        self.author = author

    def get_count(self):
        """
        Gets count of the class usage.
        :return: Count of usages.
        """
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
            """
            The following is a vowel finder. Not a verified thing to work.
            """
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


def main():
    while True:
        try:
            open_file = input("Enter a poem file name (Case Sensitive): ") + ".txt"
            if not os.path.isfile(open_file):
                open_file = "DefaultPoem.txt"
                print("Defaulting to DefaultPoem\n")
            full_file = open(open_file, 'r').read()
            poem_type = Poem(full_file)
            poem_lines = full_file.splitlines()
            a_name, a_author = poem_lines[0].split(" by ")
            poem_type.set_name(a_name)
            poem_type.set_author(a_author)
            print("Name: %s\n"
                  "Author: %s\n"
                  "Poem:\n" % (poem_type.get_name(), poem_type.get_author()))
            poem_type.is_haiku(full_file)
            cont = input("Do you wanna do another one? Y/N: ")
            if cont.upper() == "N":
                print("You checked %i poems. Thank you for using this program!" % poem_type.get_count())
                exit(0)
        except Exception as e:
            print("Error: %s" % e)

if __name__ == "__main__":
    main()
