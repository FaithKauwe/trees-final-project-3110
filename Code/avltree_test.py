from avltree import AVLTree
import unittest

# to run tests: cd Code && python3 -m pytest avltree_test.py -v
class AVLTreeTest(unittest.TestCase):

# insert one entry to an empty tree then verify that entry is found by searching for the key using search()
    def test_insert_and_search_single(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        assert tree.search("dracula") == 19

    # insert and search for multiple entries
    def test_insert_and_search_multiple(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("blood", 14)
        tree.insert("castle", 7)
        assert tree.search("dracula") == 19
        assert tree.search("blood") == 14
        assert tree.search("castle") == 7
# an entry that was not added should NOT be found and we should get None back
    def test_search_missing_key(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        assert tree.search("vampire") is None

# the tree is empty and any search should return None
    def test_search_empty_tree(self):
        tree = AVLTree()
        assert tree.search("anything") is None

# test that when the same key but different values isinserted the most recent value is replacing the former
    def test_insert_duplicate_updates_value(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("dracula", 25)
        assert tree.search("dracula") == 25

# ensure the tree size increases correctly as entries are added
    def test_size_tracking(self):
        tree = AVLTree()
        assert tree.size == 0
        tree.insert("dracula", 19)
        assert tree.size == 1
        tree.insert("blood", 14)
        assert tree.size == 2
        tree.insert("castle", 7)
        assert tree.size == 3

# ensure that a duplicate key (with differing value) does not change the tree's size
    def test_size_no_change_on_duplicate(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("dracula", 25)
        assert tree.size == 1

# test that the list of ordered pairs from the entire tree is properly returned using in_order_traversal()
    def test_in_order_traversal_sorted(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("blood", 14)
        tree.insert("castle", 7)
        tree.insert("vampire", 17)
        tree.insert("abbey", 3)
        items = tree.in_order_traversal()
        keys = [key for key, value in items]
        assert keys == ["abbey", "blood", "castle", "dracula", "vampire"]

# test that an empty tree returns an empty list when calling in_order_traversal()
    def test_in_order_traversal_empty(self):
        tree = AVLTree()
        assert tree.in_order_traversal() == []

# check that the tree is properly balanced after adding entries that would create a right leaning tree
# which is the worst case scenario for an AVL tree
    def test_balance_after_ascending_inserts(self):
        tree = AVLTree()
        for word in ["abbey", "blood", "castle", "dracula", "evil"]:
            tree.insert(word, 1)
        assert tree.root.height <= 2

# # check that the tree is properly balanced after adding entries that would create a leftleaning tree
    def test_balance_after_descending_inserts(self):
        tree = AVLTree()
        for word in ["evil", "dracula", "castle", "blood", "abbey"]:
            tree.insert(word, 1)
        assert tree.root.height <= 2

# check the balance is corrcted after entries are added thar would require double rotation
    def test_balance_after_zigzag_inserts(self):
        tree = AVLTree()
        tree.insert("castle", 1)
        tree.insert("abbey", 1)
        tree.insert("blood", 1)
        assert tree.root.height <= 1

# make sure traversal doesn't change the values associated with keys
    def test_traversal_preserves_values(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("blood", 14)
        tree.insert("castle", 7)
        items = tree.in_order_traversal()
        assert items == [("blood", 14), ("castle", 7), ("dracula", 19)]


if __name__ == '__main__':
    unittest.main()
