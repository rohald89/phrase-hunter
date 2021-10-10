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
        return [Phrase("It is not a bug it is an undocumented feature"),
                Phrase("Deleted code is debugged code"),
                Phrase("Do not comment bad code rewrite it"),
                Phrase("Java is to JavaScript what car is to carpet"),
                Phrase("First solve the problem then write the code")]

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
            if not len(guess) == 1 or guess.lower() not in string.ascii_lowercase:
                print("Please enter a valid character a-z")
                continue
            elif guess.lower() in self.guesses:
                print(f"You've already guessed {guess.lower()}. Please pick another letter")
            else:
                return guess

    def game_over(self):
        if self.missed == 5:
            print("You've lost, better luck next time!")
            print(f"The phrase was: {self.active_phrase.phrase}")
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