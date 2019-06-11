class Heap:
    def __init__(self, comparator=lambda a, b: a > b):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        # set at the end of the array and bubble up till it can't anymore
        i = len(self.storage)
        self.storage.append(value)
        self._bubble_up(i)

    def delete(self):
        # if nothing in storage return None
        if len(self.storage) == 0:
            return None
        # take a copy of max value
        high_val = self.storage[0]
        # replace zero index with last index (leaf)
        self.storage[0] = self.storage[-1]
        # remove the leaf from storage
        del self.storage[-1]
        # shift down till in place
        self._sift_down(0)
        # return deleted value
        return high_val

    def get_priority(self):
        # if no values return None
        if len(self.storage) == 0:
            return None
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
         # cannot bubble up if no parents (i=0)
        if index == 0:
            return None
        while index:
            # get the parent index
            p_i = parent_i(index)
            # if passed index value is larger swap and return Index of where is swapped to
            if self.comparator(self.storage[index],  self.storage[p_i]):
                new_p = self.storage[index]
                self.storage[index] = self.storage[p_i]
                self.storage[p_i] = new_p
                index = p_i
            # failed to swap return None
            else:
                index = None

    def _sift_down(self, index):
        pass


def left_child_i(i):
    return 2*i+1


def right_child_i(i):
    return 2*i+2


def parent_i(i):
    return (i-1)//2
