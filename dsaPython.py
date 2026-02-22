#we need to download software for running python.
# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Manually link the nodes
head = node1  # Set the first node as the head
node1.next = node2
node2.next = node3

# Traverse and print the linked list
current = head
print("Linked List elements:")
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Add a new node at the end (appending)
new_node_end = Node(40)
current = head
while current.next:
    current = current.next
current.next = new_node_end

# Traverse and print the updated linked list
current = head
print("\nLinked List after appending:")
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Add a new node at the beginning (prepending)
new_node_beginning = Node(5)
new_node_beginning.next = head
head = new_node_beginning

# Traverse and print the updated linked list
current = head
print("\nLinked List after prepending:")
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")