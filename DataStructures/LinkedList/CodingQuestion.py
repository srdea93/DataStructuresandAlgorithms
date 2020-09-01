from DataStructures import LinkedList, Node
# ----------------------------- Problem 1: Reverse a LinkedList -----------------------------
def reverse_linked_list(linkedlist):
    current_node = linkedlist.head
    next_node = None
    prev_node = None
    if current_node.next is None:
        return current_node
    while current_node is not None:
        # 1 -> 2 -> 3 -> 4
        # C    N
        # C    NP
        #
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    linked_list.head = prev_node
    return linked_list

linked_list = LinkedList()
data = [1, 2, 3, 4, 5]
for num in data:
    linked_list.append(num)
print(repr(linked_list))

print("Reversed List:")
print(repr(reverse_linked_list(linked_list)))