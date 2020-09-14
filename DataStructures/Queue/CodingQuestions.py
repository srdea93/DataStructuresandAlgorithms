# ----------------------------- Problem 1: Implement a Queue using a Stack -----------------------------
class StackQueue():
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item

    def peek(self):
        return self.queue[0]

    def empty(self):
        if not self.queue:
            return True
        return False

# ----------------------------- Problem 1: Implement a Queue using a Stack (Using 2 Stacks) -----------------------------
class StackQueue2():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, data):
        # move all data to s2 so we can add new data to the bottom of s1
        while self.s1:
            self.s2.append(self.s1.pop())
        # add data to bottom of s1
        self.s1.append(data)
        # move all data back to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        if not self.s1:
            return True
        return False
