def histogram(source_text):
    """
    Create a histogram from source text.
    Returns a list of tuples where each tuple contains (word, frequency)
    """
    # use isinstance built in function (object, type) to ensure source_text is string file that
    # ends in .txt
    if isinstance(source_text, str) and source_text.endswith('.txt'):
        with open(source_text, 'r') as file:
            text = file.read().lower()
    # if not a txt file, function can accept a string
    else:
        text = source_text.lower()

    # Example input text: "the cat sat in the hat"
    # split into words (default to split on whitespace)
    words = text.split()
    # Example words list: ["the", "cat", "sat", "in", "the", "hat"]
    
    # initialize empty dict
    word_counts = {}
    
    # get() is built in method. it checks the value at a particular key [word] and if that value doesn't exist
    # it assigns the value to zero, then add 1 to whatever that value is
    # if the key already exists, the value will be updated, if key doesn't exist, a key of [word] is created
    # in the assignment part of the line `word_counts[word]`
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    # Example word_counts after loop: {"the": 2, "cat": 1, "sat": 1, "in": 1, "hat": 1}
    
    # .items() is built in dict function that converts dicts to list of tuples, where first item is word
    # and second item is count. sorted() sorts the tuples alphabetically using the first item (word)
    # which allows binary search (where half the list is eliminated each time the search loop passes and the halves
    # get incrasingly smaller), which is much more efficient than searching through every item in the list and will reduce Big O
    # significantly to O(log n)
    # Example return value: [("cat", 1), ("hat", 1), ("in", 1), ("sat", 1), ("the", 2)]
    return sorted(word_counts.items()) 


def unique_words(histogram):
    """Return the count of unique words in the histogram"""
    # Example: if histogram = [("cat", 1), ("hat", 1), ("the", 2)]
    # Returns: 3 (three unique words)
    return len(histogram)


def frequency(word, histogram):
    """
    Return frequency of a word using binary search since histogram is sorted
    """
    # Example histogram: [("cat", 1), ("hat", 1), ("in", 1), ("sat", 1), ("the", 2)]
    # Example search: frequency("the", histogram)
    
    # at this point, histogram is a list of tuples
    # binary search algo is separating the list in half each time the loop runs and discarding the half
    # where the word is not found. each pass through the list discards another half of the remaining list
    # narrowing the search on pass of the loop, so algo doesn't have to seacrh the entire list from start to
    # finish. `left` and `right` are the varaible placeholders that keep track of the halves as the search narrows
    word = word.lower()
    left, right = 0, len(histogram) - 1
    # Example: left = 0, right = 4 (for 5-item histogram)
    
    while left <= right:
        # create a third variable, mid
        mid = (left + right) // 2
        # Example first iteration: mid = 2 (middle position)
        
        # use mid as an index for the histogram list, then grab the word value at 0th elemnt in the tuple at that index
        current_word = histogram[mid][0]
        # Example: current_word = "in" (middle word in sorted list)
        
        # if that's the word being looking for, return the frequency (which is [1] of the tuple)   
        if current_word == word:
            return histogram[mid][1]
        # if current_word comes before word alphabetically, rearrange the 'left' variable so it now becomes the
        # mid postion plus one, discarding that whole half of the list for the next search loop
        elif current_word < word:
            # Example: if searching for "the", "in" < "the", so left becomes 3
            left = mid + 1
        # otherwise alter the 'right' variable to do the same thing to that half
        else:
            # Example: if searching for "cat", "in" > "cat", so right becomes 1
            right = mid - 1
            
    # if the word isn't found in the histogram, return 0
    # Example: frequency("dog", histogram) would return 0
    return 0


if __name__ == '__main__':
    
    hist = histogram('dracula.txt')
    print(f"Unique words in Dracula: {unique_words(hist)}")
    # Example output: "Unique words in Dracula: 17669"
    
    # test the frequency of some interesting words
    print(f"Frequency of 'vampire': {frequency('vampire', hist)}")
    # Example output: "Frequency of 'vampire': 17"
    print(f"Frequency of 'dracula': {frequency('dracula', hist)}")
    # Example output: "Frequency of 'dracula': 19"
    print(f"Frequency of 'the': {frequency('the', hist)}")
    # Example output: "Frequency of 'the': 7796"

