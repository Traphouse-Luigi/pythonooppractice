import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        """Read the file, and return the number of words/lines"""
        word_file = open(file)
        self.words = self.parse(word_file)
        print(f'{len(self.words)} words read')

    def parse(self, word_file):
        """Skim through the file and create a list of words"""
        return [w.strip() for w in word_file]

    def random(self):
        """Return a random word"""
        return random.choice(self.words)


class WordFinderPlus(WordFinder):
    """Customized Wordfinder that ignores comments and blank lines"""

    def parse(self, word_file):
        return [w.strip() for w in word_file if w.strip() and not w.startswith('#')]
