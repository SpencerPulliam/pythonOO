""" WordFinder - Finds random words in a text file. """

import random

class WordFinder:
    """
    Finds random words in a text file.
    
    >>> word_finder = WordFinder("test_words.txt")
    Found 5 words in file.

    >>> word_finder.random() in ["durian", "kiwi", "jackfruit", "dragon fruit", "starfruit"]
    True

    >>> word_finder.random() in ["durian", "kiwi", "jackfruit", "dragon fruit", "starfruit"]
    True

    >>> word_finder.random() in ["durian", "kiwi", "jackfruit", "dragon fruit", "starfruit"]
    True

    """

    def __init__(self, loc):
        """ Read text file and print the number of words in the file. """

        text_file = open(loc)

        self.words = self.parse(text_file)

        print(f"Found {len(self.words)} words in file.")

    def parse(self, text_file):
        """ Parse the words in the text file and return them as a list. """

        return [word.strip() for word in text_file]

    def random(self):
        """ Return a random word from the parsed list. """

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    Improved WordFinder that ignores comments.
    
    >>> special_word_finder = SpecialWordFinder("words_with_comments.txt")
    Found 5 words in file.

    >>> special_word_finder.random() in ["xolointscuintli", "ibizan", "bichon frise", "dachshund", "alaskan malamut"]
    True

    >>> special_word_finder.random() in ["xolointscuintli", "ibizan", "bichon frise", "dachshund", "alaskan malamut"]
    True

    >>> special_word_finder.random() in ["xolointscuintli", "ibizan", "bichon frise", "dachshund", "alaskan malamut"]
    True

    >>> special_word_finder.random() in ["xolointscuintli", "ibizan", "bichon frise", "dachshund", "alaskan malamut"]
    True
        
    """

    def parse(self, text_file):
        """ Overridden parse method that also excludes comments. """

        return [word.strip() for word in text_file if word.strip() and not word.startswith("#")]
    