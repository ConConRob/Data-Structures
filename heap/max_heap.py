class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # set at the end of the array and bubble up till it can't anymore
        i = len(self.storage)
        self.storage.append(value)
        while i:
            i = self._bubble_up(i)

    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        pass

    def _bubble_up(self, index):
        # cannot bubble up if no parents (i=0)
        if index == 0:
            return None
        # get the parent index
        p_i = parent_i(index)
        # if passed index value is larger swap and return Index of where is swapped to
        if self.storage[index] > self.storage[p_i]:
            new_p = self.storage[index]
            self.storage[index] = self.storage[p_i]
            self.storage[p_i] = new_p
            return p_i
        # failed to swap return None
        return None

    def _sift_down(self, index):
        pass


def left_child_i(i):
    return 2*i+1


def right_child_i(i):
    return 2*1+2


def parent_i(i):
    return (i-1)//2
