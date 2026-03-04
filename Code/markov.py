from treemap import TreeMap
import random


class MarkovChain:

    def __init__(self, word_list):
        #The Markov chain will be a python dictionary of TreeMaps
        #Example: for "one fish two fish red fish blue fish"
        #{"one": TreeMap{fish:1}, "fish": TreeMap{"two":1, "red":1, "blue":1}, ...}
        self.markov_chain = self.build_markov(word_list)
        self.first_word = list(self.markov_chain.keys())[0]

    # builds a map of next-words for every word in the text
    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            # if the word is already there, update the count
            if current_word in markov_chain:
                markov_chain[current_word].add_count(next_word)
            # otherwise build the new treemap for it
            else:
                markov_chain[current_word] = TreeMap([next_word])

        return markov_chain

    # generate a sentence num_words long using the markov chain
    def walk(self, num_words):
        current_word = random.choice(list(self.markov_chain.keys()))
        sentence = [current_word]
        for _ in range(num_words - 1):
            histogram = self.markov_chain.get(current_word)
            if histogram is None:
                break
            current_word = histogram.sample()
            sentence.append(current_word)
        return ' '.join(sentence)

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.items())