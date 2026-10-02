'''
singly linked list:
1. create Node
2. Insert the data into the nodes
3. generate the connecion b/w the nodes
4. Traverse all the nodes



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

def traverse():
    curr = node1
    while curr:
        print(curr.data,end = " -> ")
        curr = curr.next
    print("None")
traverse()

#Operations
#1. Insertion : 3 ways
       # a) Insertion at the begining
       # b) Insertion at the end
       # c) Insertion at the specified node
# 1. Deletion
# 2. traverse
# 3. update

# a) Insertion at the begining in singly linked list:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def insert_end(head,data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

def insert_at_pos(node,data):
    if node is None:
        print("Error")
        return
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node


def traverse(head):
    curr = head
    while curr:
        print(curr.data,end = " -> ")
        curr = curr.next
    print("None")

head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)
print("insertion at the begin")
traverse(head)
print()

print("insertion at the End")         
insert_end(head, 400)
traverse(head)

print("insertion at the Position")
insert_at_pos(head, 100)
traverse(head)
'''

#Deletion : 3 ways
       # a) deletion at the begining
       # b) deletion at the end
       # c) deletion at the specified node


'''
single linked list:
1. create a node
2. inssert the data into the nodes
3. generate the connecion b/w the nodes
4. traverse all the nodes 
'''
from platform import node


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# def traverse():
#     current_node = node1
#     while current_node:
#         print(current_node.data,end = " -> " )
        
#         current_node = current_node.next
#     print(None)
# traverse()       

# Operations:
# 1. Insertion : 3 ways
    # a) Insertion at the beginning
    # b) Insertion at the end
    # c) Insertion at the specific node
# 1. deletion
# 2. traverse
# 3.update

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def insert_begin(head, data):
#     new_node = Node(data)
#     new_node.next = head
#     return new_node
# def traverse(head):
#     current_node = head
#     while current_node:
#         print(current_node.data, end=" -> ")
#         current_node = current_node.next
#     print(None)
# head = None
# head = insert_begin(head, 30)
# head = insert_begin(head, 20)
# head = insert_begin(head, 10)
# print("insertion at the beginning:")    
# traverse(head)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  
def deleteion_begin(head):
    if head is None:
        print("Error")
        return 
    new_head = head.next
    del head
    return new_head        
def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current_node = head
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node
    return head
def deleteion_end(head):
    if head is None or head.next is None:
        print("Error")
        return None
    current_node = head
    while current_node.next.next:
        current_node = current_node.next
    del_node = current_node.next
    current_node.next = None
    del del_node
def insert_at_position(node, data):
    if node is None:
        print("Error")
        return
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node
def deleteion_at_position(node):
    if node is None or node.next is None:
        print("Error")
        return
    del_node = node.next
    node.next = del_node.next
    del del_node
def traverse(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print(None)
head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)
head = insert_begin(head, 40)
head = insert_begin(head, 50)
head = insert_begin(head, 60)
head = insert_begin(head, 70)
print("insertion at the beginning:")    
traverse(head)
print()

print("insertion at the end:")
insert_end(head, 400)
traverse(head)
print()

print("insertion at a specific position:")
insert_at_position(head, 50)
traverse(head)
print()

print("deletion at the beginning:")
head = deleteion_begin(head)
traverse(head)
print()

print("deletion at the end:")
deleteion_end(head) 
traverse(head)
print()

print("deletion at a specific position:")
deleteion_at_position(head)
traverse(head)
print()