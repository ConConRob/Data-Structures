"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
  Display the whole tree. Uses recursive def.
  """

    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key,
                  f'[{self.height}:{self.balance}]',
                  'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
  Computes the maximum number of levels there are
  in the tree
  """

    def update_height(self):
        # if no node return -1
        height = 0
        if self.node:
            height += max(self.node.left.update_height() if self.node.left else 0,
                          self.node.right.update_height() if self.node.right else 0) + 1 if self.node.right or self.node.left else 0
        self.height = height
        return self.height

    """
  Updates the balance factor on the AVLTree class
  """

    def update_balance(self):
        height_r = 0
        height_l = 0
        # if left update left and track total
        if self.node.left:
            self.node.left.update_balance()
            height_l = self.node.left.height
        # if right update right and track total
        if self.node.right:
            self.node.right.update_balance()
            height_r = self.node.right.height
        # set the balance
        self.balance = height_r - height_l
    """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """

    def left_rotate(self):
        # get the nodes that need to be moved
        new_parent_node = self.node.right.node
        new_child_node = self.node
        # set the left node of the new parent to the right node of the new child
        new_child_node.right.node = new_parent_node.left.node
        # set the left node of the new parent to the new child
        new_parent_node.left.node = new_child_node
        # set the new root
        self.node = new_parent_node

    """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """

    def right_rotate(self):
        pass

    """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """

    def rebalance(self):
        pass

    """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """

    def insert(self, key):
        pass
