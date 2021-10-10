import random
import string

from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def create_phrases(self):
        return [Phrase("I love Python"),
        Phrase("testing phrases "),
        Phrase("This is another phrase"),
        Phrase("How many more do I need"),
        Phrase("This will be the last one")]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print('''
        ============================
          Welcome to Phrase Hunter
        ============================
        ''')

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"You have {5 - self.missed} out of 5 lives remaining!")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()
        self.replay()

    def get_guess(self):
        while True:
            guess = input('\nEnter a letter: ').lower()
            if len(guess) > 1 or guess.lower() not in string.ascii_lowercase:
                print("Please enter a valid character a-z")
                continue
            else:
                return guess

    def game_over(self):
        if self.missed == 5:
            print("You've lost, better luck next time!")
        else:
            print("Congrats! You've won!")

    def replay(self):
        replay = input("Would you like to play again? Y/N ")
        if replay.lower() == 'y':
            self.reset()
        else:
            print("Thanks for playing! Hope to see you back soon")
    
    def reset(self):
        self.missed = 0
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        self.start()