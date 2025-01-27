import sys
sys.path.append('../queue_and_stack')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        return self.len()


    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()

        elif self.size <= 0:
            return None

    def len(self):
        return self.size
