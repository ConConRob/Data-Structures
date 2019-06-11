"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        # if first item
        if not self.head:
            # create the node
            new_node = ListNode(value)

            self.head = new_node
            self.tail = new_node
        else:
            # insert before head
            self.head.insert_before(value)
            new_node = self.head.prev
            # make new head
            self.head = new_node
        self.length += 1

    def remove_from_head(self):
        head_node = self.head
        # check if the len is 1
        if self.length == 1:
            self.tail = None
            self.head = None
            self.length = 0
        else:
            # set the next value as the head
            self.head = head_node.next
            # remove the pointers on the head
            head_node.delete()
            self.length -= 1
            # return the old head value
        return head_node.value

    def add_to_tail(self, value):
        # cover first item case
        if self.length == 0:
            # create new node
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        # else
        else:
            # insert it after the current tail
            self.tail.insert_after(value)
            new_node = self.tail.next
            # make it the new tail
            self.tail = new_node
        # always add 1 to length
        self.length += 1

    def remove_from_tail(self):
        tail_node = self.tail
        # check if the len is 1
        if self.length == 1:
            self.tail = None
            self.head = None
            self.length = 0
        else:
            # set the next value as the head
            self.tail = tail_node.next
            # remove the pointers on the head
            tail_node.delete()
            self.length -= 1
            # return the old head value
        return tail_node.value

    def move_to_front(self, node):
        # check if is the tail
        if node == self.tail:
            # set prev to new tail
            self.tail = node.prev
        # delete node
        node.delete()
        # set as head
        self.head.insert_before(node.value)
        self.head = self.head.prev
        return self.head

    def move_to_end(self, node):
        # check if the head
        if node == self.head:
            # set next to new head
            self.head = node.next
        # delete node
        node.delete()
        # set as tail
        self.tail.insert_after(node.value)
        self.tail = self.tail.next
        return self.tail

    def delete(self, node):
        # check if head
        if self.head == node:
            # set next as head
            self.head = node.next
        # check if tail
        if self.tail == node:
            # set prev as tail
            self.tail = node.prev
        # delete node
        node.delete()
        # lower length by one
        self.length -= 1

    def get_max(self):
        # if nothing is in the list
        if self.length == 0:
            # return None
            return None
        highest = self.head.value
        current_node = self.head.next
        while current_node != None:
            # if new highest
            if current_node.value > highest:
                # set new highest
                highest = current_node.value
            # set the next node
            current_node = current_node.next
        # return the highest
        return highest
