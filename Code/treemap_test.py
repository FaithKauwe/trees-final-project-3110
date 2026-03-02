from treemap import TreeMap
import unittest

# to run the tests: python3 -m pytest treemap_test.py -v
class TreeMapTest(unittest.TestCase):

    fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

# insert one entry to an empty tree then verify the frequency of that word is 1
    def test_add_count_new_word(self):
        tm = TreeMap()
        tm.add_count("dracula")
        assert tm.frequency("dracula") == 1

# add an existing word and make sure the frequency count increases 
    def test_add_count_existing_word(self):
        tm = TreeMap()
        tm.add_count("dracula")
        tm.add_count("dracula")
        assert tm.frequency("dracula") == 2

# verify that the total count is correctly returnedwhen a duplicate word with an existing count is added
    def test_add_count_with_amount(self):
        tm = TreeMap()
        tm.add_count("dracula", 5)
        assert tm.frequency("dracula") == 5
        tm.add_count("dracula", 3)
        assert tm.frequency("dracula") == 8

# verify that 0 is returned if a word not in the map is searched for via frequency()
    def test_frequency_missing_word(self):
        tm = TreeMap()
        tm.add_count("dracula")
        assert tm.frequency("vampire") == 0

# an empty tree map returns 0 for any frequency() search
    def test_frequency_empty_treemap(self):
        tm = TreeMap()
        assert tm.frequency("anything") == 0

# verify the unique words are accurately being recorded as types
    def test_types_tracking(self):
        tm = TreeMap(self.fish_words)
        assert tm.types == 5

# verify that when duplicate words are added types count does not increase
    def test_types_no_change_on_duplicate(self):
        tm = TreeMap(self.fish_words)
        tm.add_count("fish")
        assert tm.types == 5

# verify total count of all words (tokens) is recording correctly
    def test_tokens_tracking(self):
        tm = TreeMap(self.fish_words)
        assert tm.tokens == 8

# verify that tokensincrease when a duplicate word is added
    def test_tokens_increase_on_duplicate(self):
        tm = TreeMap(self.fish_words)
        tm.add_count("fish")
        assert tm.tokens == 9

# verify the tree map is created and the frequency of words is as expected
    def test_init_with_word_list(self):
        tm = TreeMap(self.fish_words)
        assert tm.frequency("fish") == 4
        assert tm.frequency("one") == 1
        assert tm.frequency("two") == 1
        assert tm.frequency("red") == 1
        assert tm.frequency("blue") == 1

# verify that calling items() returns sorted list of key/value pairs
    def test_items_returns_sorted(self):
        tm = TreeMap(self.fish_words)
        items = tm.items()
        keys = [key for key, count in items]
        assert keys == sorted(keys)

# ensure that calling sample() returns a word thatappears in the tree map
    def test_sample_returns_valid_word(self):
        tm = TreeMap(self.fish_words)
        for _ in range(100):
            word = tm.sample()
            assert word in ["one", "fish", "two", "red", "blue"]

# verify the weighted distrubtions are working
    def test_sample_weighted_distribution(self):
        tm = TreeMap(self.fish_words)
        samples_list = [tm.sample() for _ in range(10000)]
        fish_count = samples_list.count("fish")
        fish_freq = fish_count / len(samples_list)
        expected_freq = 4 / 8
        assert expected_freq * 0.9 <= fish_freq <= expected_freq * 1.1


# verify the requested range of alphabetical responses is correctly returned
    def test_range_query(self):
        tm = TreeMap()
        for word in ["abbey", "blood", "castle", "dracula", "evil"]:
            tm.add_count(word)
        results = tm.range_query("blood", "dracula")
        keys = [key for key, count in results]
        assert keys == ["blood", "castle", "dracula"]

# if the range query has no matches, should return an empty list
    def test_range_query_no_matches(self):
        tm = TreeMap()
        for word in ["abbey", "blood", "castle"]:
            tm.add_count(word)
        results = tm.range_query("dog", "fish")
        assert results == []

# make sure the prefix search is grabbing the right words
    def test_prefix_search(self):
        tm = TreeMap()
        for word in ["van", "vampire", "vampires", "vampiric", "vast"]:
            tm.add_count(word)
        results = tm.prefix_search("vamp")
        keys = [key for key, count in results]
        assert keys == ["vampire", "vampires", "vampiric"]

# if there are no matches for prefix search, should return empty list 
    def test_prefix_search_no_matches(self):
        tm = TreeMap()
        for word in ["abbey", "blood", "castle"]:
            tm.add_count(word)
        results = tm.prefix_search("zom")
        assert results == []


if __name__ == '__main__':
    unittest.main()
