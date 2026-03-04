from treemap import TreeMap
from markov import MarkovChain
import time

# run python3 demo.py from the Code/ directory.

# reads the file, returns clean list of words
def load_words(filename):
    import re
    with open(filename, 'r') as f:
# convert everything to lowercase
        text = f.read().lower()
# use regex to strip out punctuation and numbers
    words = re.findall(r"[a-z']+", text)
    return words


def divider(title):
    print()
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)
    print()


def main():
    print("Loading Dracula by Bram Stoker...")
    words = load_words('dracula.txt')
    print(f"Total words in text: {len(words)}")

    divider("1. BUILDING TREEMAP (AVL Tree-backed word frequency map)")

    # load the clean list of words into the treemap
    start = time.time()
    tm = TreeMap(words)
    elapsed = time.time() - start
    print(f"Unique words (types): {tm.types}")
    print(f"Total words (tokens): {tm.tokens}")
    print(f"AVL tree root height: {tm.tree.root.height}")
    print(f"TreeMap built in {elapsed:.3f} seconds")

    divider("2. WORD FREQUENCY LOOKUPS — O(log n) guaranteed")

    search_words = ["dracula", "vampire", "blood", "night", "castle", "the", "love"]
    for word in search_words:
        count = tm.frequency(word)
        print(f"  '{word}' appears {count} times")

    divider("3. RANGE QUERY — words between 'blood' and 'castle'")

    results = tm.range_query("blood", "castle")
    print(f"  Found {len(results)} words in range ['blood' ... 'castle']")
    print(f"  First 10: {results[:10]}")
    print(f"  Last 10:  {results[-10:]}")

    divider("4. PREFIX SEARCH — all words starting with 'vamp'")

    results = tm.prefix_search("vamp")
    print(f"  Words starting with 'vamp': {results}")
    print()
    results = tm.prefix_search("drac")
    print(f"  Words starting with 'drac': {results}")
    print()
    results = tm.prefix_search("night")
    print(f"  Words starting with 'night': {results}")

    divider("5. ALPHABETICAL WORD REPORT (first 20 words)")

    for i, (word, count) in enumerate(tm.items()):
        if i >= 20:
            print("  ...")
            break
        print(f"  {word:<20} {count:>5}")

    divider("6. MARKOV CHAIN SENTENCE GENERATION (powered by TreeMap)")

    print("Building Markov chain...")
    start = time.time()
    mc = MarkovChain(words)
    elapsed = time.time() - start
    print(f"Words in chain: {len(mc.markov_chain)}")
    print(f"Markov chain built in {elapsed:.3f} seconds")
    print()
    for i in range(5):
        sentence = mc.walk(15)
        print(f"  Sentence {i+1}: {sentence}")
        print()

    divider("7. PREFIX SEARCH — TreeMap vs Markov Chain")

    prefix = "night"
    print(f"  Prefix: '{prefix}'")
    print()
    print(f"  TreeMap (whole book frequencies):")
    for word, count in tm.prefix_search(prefix):
        print(f"    {word:<20} {count:>5}")
    print()
    print(f"  Markov Chain (what follows 'night'):")
    night_histogram = mc.markov_chain.get(prefix)
    if night_histogram:
        for word, count in night_histogram.items():
            print(f"    {word:<20} {count:>5}")

    divider("8. ALL TESTS PASSING")

    import subprocess
    subprocess.run(["python3", "-m", "pytest", "avltree_test.py", "treemap_test.py", "-v"])


if __name__ == '__main__':
    main()
