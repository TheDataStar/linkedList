# CS233T Unit 1 Submission 2 - Linked Lists. Adam G. (22579036), [June, 2020].
# The deque object is a double ended queue. It is an implementation of a linked list which can access insert and remove elements.


# First way to create a linked list.
from collections import deque   #called the collections module to import a deque "deck" object.

linkedList = deque(["node1", "node2", "node3"]) #named and populated the deque object with sequential node values 1 through 3.

linkedList.append("node4") # appended list to add fourth node.

print(linkedList)

# Second way to create a linked list. Creating a class for linked list and defining its properties allows for more control and visual representation of NULL value at tail.
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList2:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

lList = linkedList2()

first_node = node("node1")
lList.head = first_node

second_node = node("node2")
third_node = node("node3")
fourth_node = node("node4")

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

print(lList)
