class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # set at the end of the array and bubble up till it can't anymore
        i = len(self.storage)
        self.storage.append(value)
        self._bubble_up(i)

    def delete(self):
        # if nothing in return None
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

    def get_max(self):
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
            if self.storage[index] > self.storage[p_i]:
                new_p = self.storage[index]
                self.storage[index] = self.storage[p_i]
                self.storage[p_i] = new_p
                index = p_i
            # failed to swap return None
            else:
                index = None

    def _sift_down(self, index):
        # if index does not exist return
        if index >= len(self.storage):
            return None
        while True:
            # get children index's and values
            i_r = right_child_i(index)
            v_r = self.storage[i_r] if i_r < len(self.storage) else None
            i_l = left_child_i(index)
            v_l = self.storage[i_l] if i_l < len(self.storage) else None
            # check which has larger value
            i_h = None
            v_h = None
            if v_r is None and v_l is None:
                break
            elif v_r is None:
                i_h = i_l
                v_h = v_l
            elif v_l is None:
                i_h = i_r
                v_h = v_r
            # both values exist
            else:
                # check if that value is larger
                i_h = i_r if v_r >= v_l else i_l
                v_h = v_r if v_r >= v_l else v_l
            # check the high value vs the current index
            if self.storage[index] < v_h:
                # swap values
                self.storage[i_h] = self.storage[index]
                self.storage[index] = v_h
                # return new i of shifted down
                index = i_h
            # break if no swap
            else:
                break


def left_child_i(i):
    return 2*i+1


def right_child_i(i):
    return 2*i+2


def parent_i(i):
    return (i-1)//2
