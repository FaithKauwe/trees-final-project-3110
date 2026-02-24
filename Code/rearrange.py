import random
import sys

def rearrange_words(words):
    """Randomly rearranges a list of words."""
    # Convert to list if it's not already (in case we get a tuple)
    word_list = list(words)
    # Shuffle the list in place
    random.shuffle(word_list)
    # Return the shuffled words joined into a string
    return ' '.join(word_list)

if __name__ == '__main__':
    # Check if words were provided as command-line arguments
    if len(sys.argv) > 1:
        # sys.argv[1:] gets all command line arguments after the script name
        words = sys.argv[1:]
        rearranged_words = rearrange_words(words)
        print(rearranged_words)
    else:
        print("Please provide words to rearrange as command-line arguments")

