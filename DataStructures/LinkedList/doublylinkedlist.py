from DataStructures import Node
class DoublyLinkedList():
    def __iter__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.head is None:
            return None
        else:
            node = self.head
            nodes = ""
            while node.next != None:
                if node.prev is None:
                    pass
                else:
                    nodes += F"{node.prev.data} <- "
                nodes += F"{node.data} -> "
                node = node.next
            nodes += F"{node.data} -> "
            nodes += "None"
        return nodes

    def prepend(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            self.head.next = None
            self.head.prev = None
        if self.tail is None:
            self.tail = node
            self.tail.next = None
            self.tail.prev = None
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            self.head.next = None
            self.head.prev = None
        if self.tail is None:
            self.tail = node
            self.tail.next = None
            self.tail.prev = None
        else:
            node.prev = self.tail.prev
            self.tail.next = node
            self.tail = node

    def lookup(self, data):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == data:
                return cur_node
            else:
                cur_node = cur_node.next
        return None

# Not fully implemented as doubly linked list
    def insert(self, index, data):
        node = Node(data=data)
        cur_node = self.head
        cur_index = 0
        while cur_index < index - 1 and cur_node is not None: #O(n)
            cur_node = cur_node.next
            cur_index += 1
        cur_node.prev = node
        node.next = cur_node.next
        cur_node.next = node

    def remove(self, data):
        cur_node = self.head
        prev_node = None
        while cur_node is not None:
            if cur_node.data == data:
                prev_node.next = cur_node.next
                return data
            else:
                prev_node = cur_node
                cur_node = cur_node.next
        return None