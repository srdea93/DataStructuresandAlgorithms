class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next