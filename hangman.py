import sys
import time
import random

class hangman:

# imports file containing the words for hangman
    def import_words(self, file_path):
        list_of_words = ()
        file = open(file_path, 'r')
        words = file.read().splitlines()
        return words

    def __init__(self):
        self.words = self.import_words('words.txt')
        self.games_played = 0
        self.limit = len(self.words) - 1

# Asks user if he wants to play
    def prompt_start(self):
        while True:
            r = input('Ready to play? (y/n)')
            if r == 'n':
                print('Why are you here?')
                time.sleep(1)
                sys.exit()
            elif r != 'y':
                print('Please enter valid input.')
                time.sleep(1)
            else:
                print('Here We Go!')
                return

    #facilitates removal of character
    def remove(self, list_word, char):
        change = False
        for index, ch in enumerate(list_word):
            if ch == char:
                self.current_places[index] = ch
                self.correct_letters += 1
                list_word[index] = '_'
                change = True
        return change


    # facilitates game
    def hang(self, word):
        self.current_word = list(word)
        self.current_places = {} # make it number: '_'
        self.correct_letters = 0
        for i in range(len(self.current_word)):
            self.current_places[i] = '_'
        try_num = 0
        while try_num < 8:
            self.print_game()
            letter = input('Enter a letter: ')
            letter_removed = self.remove(self.current_word, letter)
            if letter_removed:
                print('You guessed correctly!')
            else:
                print('Incorrect, you lost a life!')
                try_num += 1
            if len(self.current_word) == self.correct_letters:
                print('Congrats, you guess the word!')
                return True
        print('Oh no you are out of tries! You died :(')
        return False

    def print_game(self):
        for key, value in self.current_places.items():
            print(value, end=' ')
        print('\n', end='')

if __name__ == '__main__':
    print('Welcome to HANGMAN')
    game = hangman()
    game.prompt_start()
    while game.games_played < game.limit:
        word_number = random.randint(0, game.limit - game.games_played)
        win = game.hang(game.words[word_number])
        if win is False:
            print('You died, unlucky mate...')
            time.sleep(1)
            sys.exit()
        print('You survived!')
        game.prompt_start()
        game.games_played += 1
        game.words.remove(game.words[word_number])


    print('Out of words, thanks for playing!')
