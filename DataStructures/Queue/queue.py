# Implement a queue using a linked list
from DataStructures import LinkedList


class Queue():
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, data):
        self.items.prepend(data=data)

    def dequeue(self):
        if self.items.tail.data:
            item = self.items.tail.data
            self.items.remove(item)
            return item
        return None

    def peek(self):
        if self.items.tail.data:
            return self.items.tail.data
        return None

    def lookup(self, data):
        while self.items.head.data:
            if self.items.head.data == data:
                return data
            else:
                self.items.head = self.items.head.next
        return None

