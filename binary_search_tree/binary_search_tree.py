class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # check if higher
        if value > self.value:
            # check if right
            if self.right:
                # insert into right tree
                self.right.insert(value)
            # create new tree and set as right
            else:
                self.right = BinarySearchTree(value)
        # if lower
        elif value < self.value:
            # check if left
            if self.left:
                # insert into left tree
                self.left.insert(value)
            # create new tree and set as left
            else:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        # return true if value = target
        if target == self.value:
            return True
        # check if higher
        elif target > self.value:
            # check if right exists
            if self.right:
                # return call contains on right
                return self.right.contains(target)
            # return false
            return False
        # it is lower
        else:
            # check if left exists
            if self.left:
                # return call contains on left
                return self.left.contains(target)
            # return False
            return False

    def get_max(self):
        # check if right
        if self.right:
            # return get max for it
            return self.right.get_max()
        # return value
        return self.value

    def for_each(self, cb):
        # run cb
        cb(self.value)
        # check left
        if self.left:
            # call for each for left
            self.left.for_each(cb)
        # check right
        if self.right:
            # call for each for right
            self.right.for_each(cb)
