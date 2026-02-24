import random

# python module that allows access to command line args (among other things)
import sys

def read_words_file():
    """Read words from the Unix words file. Once the with block ends, the connection to the file terminates. NO local copy of the file is created"""
    words_list = []
    # split the file on each line and add each word to the words_list
    with open('/usr/share/dict/words', 'r') as file:
        words_list = file.read().splitlines()
    return words_list

def create_random_sentence(num_words, words_list):
    """Create a 'sentence' with the specified number of random words."""
    if num_words > len(words_list):
        return "Error: Requested more words than available"
    
    # select random words
    selected_words = random.sample(words_list, num_words)
    
    # join words with spaces and add period at the end to simulate a real sentence
    return ' '.join(selected_words) + '.'

if __name__ == '__main__':
    # sys.argv is how user input is collected and is stored as a list of 2 strings. 
    # [0] is the file name and [1] is the number of words to be output in the sentence
    # if the length of the list is not exactly 2, it means no num arg was provided
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <number_of_words>")
        sys.exit(1)
    
    try:
    # access the number the user input, stored as string so must be converted to int
        num_words = int(sys.argv[1])
        if num_words < 1:
            print("Please enter a positive number")
    # exit the program after prinitng the error
            sys.exit(1)
    except ValueError:
        print("Please enter a valid number")
        sys.exit(1)

    # read words file
    words_list = read_words_file()
    
    # generate and print random sentence
    sentence = create_random_sentence(num_words, words_list)
    print(sentence)

