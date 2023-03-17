import ipdb

class Anagram:

    def __init__(self, word):
        self.word = word
        self.matching_words = []
    
    def match (self, wordlist):

        for eachWord in wordlist:
            if sorted(list(eachWord)) == sorted(list(self.word)):
                self.matching_words.append(eachWord)

        return self.matching_words