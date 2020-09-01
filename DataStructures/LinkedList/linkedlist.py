from DataStructures import Node
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.head is None:
            return None
        else:
            node = self.head
            nodes = ""
            while node.next != None:
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
        if self.tail is None:
            self.tail = node
            self.tail.next = None
        else:
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            self.head.next = None
        if self.tail is None:
            self.tail = node
            self.tail.next = None
        else:
            self.tail.next = node
            self.tail = node

    def insert(self, index, data):
        node = Node(data=data)
        cur_node = self.head
        cur_index = 0
        while cur_index < index - 1 and cur_node is not None: #O(n)
            cur_node = cur_node.next
            cur_index += 1
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



# ------------------------ Test ------------------------
linked_list = LinkedList()
data = [1, 2, 3]
for num in data:
    linked_list.append(num)

linked_list.insert(2, 4)
linked_list.remove(4)

print(repr(linked_list))