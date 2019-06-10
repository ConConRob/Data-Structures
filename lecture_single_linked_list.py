# node class to hold value and a ref to the next node in a chain


class Node:
    def __init__(self, value=None, next_node=None):
        # set value at this node
        self.value = value
        # set ref to the next node in the chain
        self.next_node = next_node

    # get the value of the current node
    def get_value(self):
        return self.value

    # get the ref to the next node in the chain
    def get_next(self):
        return self.next_node

    # set the ref to the next node in the chain
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # set init ref to the head
        self.head = None
        # set init ref to the tail
        self.tail = None

    def add_to_tail(self, value):
        # wrap the val inside a node
        new_node = Node(value, None)
        # 1. the lists empty
        # check if no head
        if not self.head:
            # set head and tail to new node
            self.head = new_node
            self.tail = new_node
        # if not empty
        else:
            # add a new node to the tail
            self.tail.set_next(new_node)
            # set the tails next ref to out new_node
            # set the tail's tail ref to the new node
            self.tail = new_node

    def remove_head(self):
        # return None if no head
        if not self.head:
            return None
        # if sigle node list
        if not self.head.get_next():
            # get ref to the head
            head = self.head
            # set head and tail to None
            self.head = None
            self.tail = None
            return head.get_value()

        # otherwise store and set next
        head = self.head
        self.head = head.get_next()
        return head.get_value()

    def contains(self, value):
        # return False if no head
        if not self.head:
            return False
        # get the ref to node we are currently at
        node = self.head

        while node:
            if node.get_value() == value:
                return True
            # set the next node
            node = node.get_next()

        return False
