class Node:
# each node holds one key/ value pair (like an entry in a dict) and pointers to 2 children
    def __init__(self, key, value):
# the key is the word 
        self.key = key
# value is the frequency count
        self.value = value
        self.left = None
        self.right = None
# height is how tall the subtree at this node is, will be used to detect imbalance
        self.height = 0


class AVLTree:
# the AVL tree doesn't actually store any data, it stores pointers to the nodes and the nodes
# themselves store the data
    def __init__(self):
# root is the top node of the tree, starts as None (empty). Every operation begins here
# and works downward
        self.root = None
# size is how many key/value pairs are in the tree, gets increased with the insert function
        self.size = 0
    
# reads the height attribute stored on the node and safely returns a -1 value if the node is None (rather than breaking)
    def _height(self, node):
        if node is None:
            return -1
        else:
            return node.height

# uses the safe _height wrapper to access the node's numerical left and right values and calculate their diff
# returns the number value of that diff
    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

# odes height uses the safe wrapper, then adds 1 to whichever of those heights 
# (left or right) is larger and sets that as the new height of that node
# method gets called anytime the tree structure changes, the effected nodes need their heights relcaluclated so
# _balance_factor stays accurate
    def _update_height(self, node):
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        node.height = 1 + max(left_height, right_height)

    def _rotate_right(self, node):
    # left node becomes the new root
        new_root = node.left
    # the new root's left node gets reassigned 
        node.left = new_root.right
    # original root node now becomes the right child
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

# even though each roatation only has 3 moves, those 3 moves will reorder the whole tree bc each node could represent a whole subtree    
    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rebalance(self,node):
        balance_factor_number = self._balance_factor(node)
# if it's leaning left
        if balance_factor_number > 1:
# an inner check to see if the branch is zig zagged and needs a double rotation to fix it
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
# if it's leaning right
        elif balance_factor_number < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
# if it's already balanced 
        else:
            return node

# insert's one job is just to reassign whatever gets returned from _insert and as the new self.root
# it's a public wrapper that kicks off the recursive _insert helper
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

# _insert is taking a key/value pair and checking if it exists in the tree, running down the whole length
# if it doesn't exist, it finds a new spot to put it (as a new node) and chooses where it will go based on sorted order
# the tree will get balanced on the way back up the recursive call, through _update_height and _rebalance
# if the pair already exists, will replace the current value with whatever value is passed in through the function param
    def _insert(self, node, key, value):
    # this is the base case, all the lower recursive calls will finish when they reach this, which is finding
    # an empty spot for the new node to go 
        if node is None:
    # create a new Node using the provided key/ value pair
            new_node = Node(key,value)
    # increase the size of the tree
            self.size += 1
            return new_node
    # choose where to place the node based on sorting order
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
    # the word already exists, just updating the count held in value
        elif key == node.key:
            node.value = value
    # climb back up the tree and balance the tree as needed
        self._update_height(node)
        return self._rebalance(node)
        
# search is the public wrapper that kicks off the recursive _search and just returns whatever _search finds
# we use the public wrapper to align with encapsulation pricibples so that things outside the class can stay clean, simple method calls
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
    # the key isn't in the tree
        if node is None:
            return None
    # found the key and returning it
        elif key == node.key:
            return node.value
    # choose which branch to recursicvely search down based on the ordering of key
        elif key < node.key:
    # _insert had to assign and organize things on the climb back up, but _search just has to return the found value
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)

    # public wrapper that kickstarts the private recursive helper, yields all key value pairs in sorted order
    def in_order_traversal(self):
        items = []
        self._in_order(self.root, items)
        return items

    # the order is important. left of the node, the node itself, right of the node. bc the tree is already sorted, just visting the nodes in this order yields a sorted list
    def _in_order(self, node, items):
    # the base case, which finds the "edge" ofthe tree where the node has no left child (if recursing left) or right child (if recursing right)
        if node is None:
            return
    # recurse left, visit everything smaller first
        self._in_order(node.left, items)
    # add this node's key/valuepair as atuple to the list. there's only one append call needed bc of the recursive structuring.  every node in the tree will eventually be the 
    # (node) param in _in_order. A sub node won't get added to the items list. it will only get added when it's that node's turn to play the part of the param
        items.append((node.key, node.value))
    # recurse right, visit everything larger after
        self._in_order(node.right, items)
