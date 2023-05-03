import ipdb


class Anagram:
    def __init__(self, word):
        self.word = sorted(word)

    def match(self, word_list):
        return list(word for word in word_list if sorted(word) == self.word)
