from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = None
        self.guesses = [" "]

    def create_phrases(self):
        return [Phrase("I love Python"),
        Phrase("testing phrases "),
        Phrase("This is another phrase"),
        Phrase("How many more do I need"),
        Phrase("This will be the last one")]
