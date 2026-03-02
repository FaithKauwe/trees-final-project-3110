from avltree import AVLTree
import random


class TreeMap:

    def __init__(self, word_list=None):
        self.tree = AVLTree()
        # count of distinct word types in this histogram
        self.types = 0
        # count of all the words total
        self.tokens = 0
        # count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        # search the tree for the word
        existing = self.tree.search(word)
        # if the word exists, update its value with insert (AVL tree's duplicate key replaces value will update the value without changing the key)
        if existing is not None:
            self.tree.insert(word, existing + count)
        # if the word is new, insert it andincrease types count
        else:
            self.tree.insert(word, count)
            self.types += 1
        # increase tokens count either way
        self.tokens += count

# will return the number of times the inuque word appears in the list
    def frequency(self, word):
# search() ultimately returns the value of the node, which is the count, so just storing the return value in result and then returning it works
        result = self.tree.search(word)
        if result is None:
            return 0
        return result

    def sample(self):
        #Randomly choose a word based on its frequency in this histogram
        # get total number of words to use in range
        total_tokens = self.tokens
        random_value = random.randint(1, total_tokens)
        cumulative = 0
        # tree method .in_order_traversal() returns key/value pairs as tuples of the 2 items
        for word, count in self.tree.in_order_traversal():
        # cumulative now = count in the tuple
            cumulative += count
        # if cumulative is larger than random_value, return the word
        # more frequent words get larger ranges
            if random_value <= cumulative:
                return word

    def items(self):
        return self.tree.in_order_traversal()