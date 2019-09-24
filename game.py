import random

class Game():
    def __init__(self):
        List_Alphabet = ["A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.grid = random.choices(List_Alphabet, k=9)
        #print (self.grid)

    def is_valid(self, word):
        user_word = ""
        if not word:
            print("there is no word")
            return False
        for letter in word:
            if letter in self.grid:
                user_word = user_word + letter
                self.grid.remove(letter)
            else:
                print(letter + " is not present in your grid")
                return False
        print("you word : " + user_word + " uses grid's letters")
        return True
