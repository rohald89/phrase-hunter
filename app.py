# Import your Game class
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase
# Create your Dunder Main statement.
if __name__ == '__main__':
    # phrase = Phrase()
    game = Game()
    phrase = Phrase('Life is like a box of chocolates')
    for phrase in game.phrases:
        print(phrase.phrase)
        
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
