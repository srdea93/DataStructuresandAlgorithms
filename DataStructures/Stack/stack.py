# Build a stack with an array
class Stack():
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        item = self.data[-1]
        self.data = self.data[:-1]
        return item

    def peek(self):
        item = self.data[-1]
        return item

    def lookup(self, item):
        if self.data:
            for data in self.data:
                if data == item:
                    return data
        return None
