from avltree import AVLTree
import unittest


class AVLTreeTest(unittest.TestCase):

    def test_insert_and_search_single(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        assert tree.search("dracula") == 19

    def test_insert_and_search_multiple(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("blood", 14)
        tree.insert("castle", 7)
        assert tree.search("dracula") == 19
        assert tree.search("blood") == 14
        assert tree.search("castle") == 7

    def test_search_missing_key(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        assert tree.search("vampire") is None

    def test_search_empty_tree(self):
        tree = AVLTree()
        assert tree.search("anything") is None

    def test_insert_duplicate_updates_value(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("dracula", 25)
        assert tree.search("dracula") == 25

    def test_size_tracking(self):
        tree = AVLTree()
        assert tree.size == 0
        tree.insert("dracula", 19)
        assert tree.size == 1
        tree.insert("blood", 14)
        assert tree.size == 2
        tree.insert("castle", 7)
        assert tree.size == 3

    def test_size_no_change_on_duplicate(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("dracula", 25)
        assert tree.size == 1

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

    def test_in_order_traversal_empty(self):
        tree = AVLTree()
        assert tree.in_order_traversal() == []

    def test_balance_after_ascending_inserts(self):
        tree = AVLTree()
        for word in ["abbey", "blood", "castle", "dracula", "evil"]:
            tree.insert(word, 1)
        assert tree.root.height <= 2

    def test_balance_after_descending_inserts(self):
        tree = AVLTree()
        for word in ["evil", "dracula", "castle", "blood", "abbey"]:
            tree.insert(word, 1)
        assert tree.root.height <= 2

    def test_balance_after_zigzag_inserts(self):
        tree = AVLTree()
        tree.insert("castle", 1)
        tree.insert("abbey", 1)
        tree.insert("blood", 1)
        assert tree.root.height <= 1

    def test_traversal_preserves_values(self):
        tree = AVLTree()
        tree.insert("dracula", 19)
        tree.insert("blood", 14)
        tree.insert("castle", 7)
        items = tree.in_order_traversal()
        assert items == [("blood", 14), ("castle", 7), ("dracula", 19)]


if __name__ == '__main__':
    unittest.main()
