class BSTNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = BSTNode(data=data)
        if self.root:
            cur_node = self.root
            while cur_node:
                if node.data < cur_node.data:
                    print(F"{node.data} is less than {cur_node.data}")
                    if cur_node.left is None:
                        cur_node.left = node
                        print(F"inserting {data}")
                        break
                    else:
                        cur_node = cur_node.left

                else:
                    print(F"{node.data} is greater than {cur_node.data}")
                    if cur_node.right is None:
                        cur_node.right = node
                        print(F"inserting {data}")
                        break
                    else:
                        cur_node = cur_node.right
        else:
            self.root = node
            print(F"root = {node.data}")

    def lookup(self, data):
        cur_node = self.root
        while cur_node is not None:
            if cur_node.data == data:
                return cur_node
            elif cur_node.data > data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return None

    def remove(self, data):
        pass
        remove_node = self.lookup(data)
        replace_node = None
        # if we don't find the data to be removed
        if not remove_node:
            return None
        else:
            replace_node = remove_node.left
            while replace_node:
                replace_node = replace_node.left



# ------------------------ Test ------------------------
bst = BinarySearchTree()
data = [9,4,3,2,1,19,24]
for num in data:
    bst.insert(num)

print(bst.lookup(5).data)
print(bst.lookup(19).data)



