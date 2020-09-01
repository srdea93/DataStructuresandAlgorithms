class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        if self.prev is None:
            return F"{self.data} -> {self.next.data}"
        else:
            return F"{self.prev.data} <- {self.data} -> {self.next.data}"

    def set(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev