from pickle import TRUE
import random

class SecretWord:
    def __init__(self, _secret_word:str = "None"):
        if _secret_word == "None":
            with open('week02/words.txt', 'r') as file:
                text = file.read()
                words = list(map(str, text.split()))
                self._secret_word = (random.choice(words))
        else:
            self._secret_word = _secret_word.upper()
    
    def show_letters(self, letters):
        my_string = self._secret_word.upper()

        my_string = len(self._secret_word) * "_ "
        for item in letters:
            index = 0
            for char in self._secret_word.upper():
                if char == item:
                    my_string = my_string[:index] + char + my_string[index + 1:]
                index += 2
        my_string = my_string[:-1]

        return my_string

    def check_letters(self, letters):
        if all(chars in letters for chars in self._secret_word):
            return True
        else:
            return False

    def check(self, string:str):
        if self._secret_word.upper() == string.upper():
            return True
        else:
            return False

class Game:

    def __init__(self, turns):
        self.secret_word = SecretWord()
        self.letters = []
        self.turns = turns

    def play_one_round(self):

        userInput = input("Geuss a letter").upper()
        self.letters.append(userInput)

        if userInput in self.letters:
            userInput = input("Letter has already been Guessed another letter")

        SecretWord.show_letters(self.letters)

        if self.secret_word.check_letters(self.letters) == TRUE:
            print("You have geussed all the words \n YOU WIN")
        else:
            print("You LOSE")

        userCheck = input("Player check your word. \n type the word you think it is")

        if SecretWord.check(userCheck) == TRUE:
            print("Word was correctly Guessed CONGRATS")


    def play(self):
        while self.turns > 0:
            self.turns -= 1
            self.play_one_round()
            