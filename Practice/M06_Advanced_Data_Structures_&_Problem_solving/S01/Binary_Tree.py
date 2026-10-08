'''Tree
Trees ard non linear data structures that are used to represent hierarchical relationships between elements. A tree consists of nodes connected by edges, where each node can have zero or more child nodes. The topmost node is called the root, and nodes with no children are called leaves. Trees are widely used in computer science for various applications such as representing file systems, organizing data for efficient searching and sorting, and implementing algorithms like binary search trees and heaps.
node contains of three parts:
1. Data: The value or information stored in the node.
2. Left Child: A reference to the left child node.
3. Right Child: A reference to the right child node.
representation of tree:

        1
       / \
      2   3
     / \
    4   5
key components of a tree:
1. Root: The topmost node of the tree, which serves as the starting point for traversing the tree.
2. Parent: A node that has one or more child nodes.
3. Child: A node that is a descendant of another node, connected by an edge.
4. Leaf: A node that has no children, representing the end of a branch in the tree.
5. Depth: The number of edges from the root to a particular node, indicating its level in the tree.
6. node: An individual element in the tree that contains data and references to its child nodes.    
Tpes of trees:
1. Binary Tree: A tree in which each node has at most two children, referred to as the left child and the right child.  
2. Binary Search Tree (BST): A binary tree in which the left child of a node contains values less than the node's value, and the right child contains values greater than the node's value. This property allows for efficient searching, insertion, and deletion operations.   
3. AVL Tree: A self-balancing binary search tree where the heights of the left and right subtrees of any node differ by at most one. This balancing ensures that the tree remains efficient for searching and other operations.
4. Red-Black Tree: A self-balancing binary search tree that maintains balance through color properties assigned to each node. It ensures that the longest path from the root to a leaf is no more than twice the length of the shortest path, providing efficient search, insertion, and deletion operations.

Applications of trees:
1. Hierarchical Data Representation: Trees are used to represent hierarchical relationships, such as file systems, organizational structures, and family trees.
2. HTML and XML Document Parsing: Trees are used to parse and represent the structure of HTML and XML documents, allowing for efficient navigation and manipulation of elements.
2. Expression Evaluation: Trees are used to represent mathematical expressions, where each node represents an operator or operand. This allows for efficient evaluation of expressions using techniques like postfix or prefix notation.
3. Decision Making: Trees are used in decision-making algorithms, such as decision trees and game   trees, to model and analyze various scenarios and outcomes.


#binary tree
#A Binaary tree is a tree it contains at most two children for each node. The left child and the right child.
# 0children,1 child,2 children not more than 2 children
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
'''
''''
Monotonic of stacks:
Arranging of elements in a particular either in increasing or decreasing
2 ways
1. Monotomic of Increase order--> small to large
2. Monotomic of Decrease order--> large to small
'''
# 1. Monotomic of Increase order--> small to large
'''Algorithm:
1. Initialize an empty stack
2. Itererate every element
3. for every element:
    -->stack should not empty and top element shopuld be greater than your curr elem
         --> Remove the element
4. insert the curr element
5. In the output it will be monotonic of increasing order elements
'''
'''def monotonic_increase(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack
arr = [1,3,2,4,5]
print(monotonic_increase(arr))'''

# 2. Monotomic of decrease order--> large to small
'''Algorithm:
1. Initialize an empty stack
2. Itererate every element
3. for every element:
    -->stack should not empty and top element should be less than your curr elem
         --> Remove the element
4. insert the curr element
5. In the output it will be monotonic of decreasing order elements
'''
'''
def monotonic_decrease(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    return stack
arr = [10,80,20,30,40,60,10]
print(monotonic_decrease(arr))

#Where We apply Monotonic of stacks:
#1. To Find the next greater Element
#2. To Find the next smaller Element
#3. To Find the previous greater element
#4. To Find the Previous smaller Element

#1. To Find the next greater Element:
#Brute Force Algorithm:
'''
'''1. Find the len of arr
2. create an result array with -1 values
3. iterate through each element throught the next right elements
4. check with the condition (if arr[j] > arr[i])
5. Store the arr[j] value in result
6. after iteration return result array'''
'''#[10,30,50,2,25]-->O/P : [50,50,-1,25,-1]
def next_greater(arr):
    n = len(arr)
    res = [-1] * n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    return res
arr = [5,3,50,2,25]
print(next_greater(arr))
'''

#Optimal Solution Algorithm:Next Greater Element
'''
1. Find the length of array
2. Create a res of array of size n,with -1
3. create an empty stack
4. Traverse the array from left to right
5. For every index:
       -->While stack is not empty and arr[stack[-1]] < arr[i]:
           -->Pop the top index
           -->Store arr[i] as next greater elem
6. After traversal, all indexes remaining in the stack,returns -1
7. Return Res array
'''
'''
def next_greater2(arr):
    n = len(arr)
    res = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            res[index] = arr[i]
        stack.append(i)
    return res
arr = [2,1,2,5,8]
print(next_greater2(arr))

#next smaller Elem:
#Previous Greater Elem:
#Previous Smaller Elem:
''' 
'''
Tree : Trees are non -linear DS
--> Non -linear : the data can be arranged in non-sequential
--> The data can be store in nodes
-->Node contains of 3 parts
   -->1. data part
   -->2. Left part
   -->3. Right part

Representation of Tree:

            10  --->Level 0
           /  \
          20   30  ---->Level 1
         / \     \
       40  50    60   ---->Level 2

Key Components:
1. Node --> Contains the data
2. Root --> Top Node is called as Root node (10)
3. Edges --> Links or connection btw the nodes
4. Parent/child --> One node derived from another(20-Parent node and 40-child node)
5. Siblings --> Two child nodes with a single parent node(20-parent and 40,50 are siblings)
6. Levels --> 
7. Height --> Height of tree 

Applications of Tree:
1. File System
2. HTML Tags
3. School Management

Types of Tree:
1. Binary Tree
2. Binary Search Tree
3. N-ary Tree
4. AVL Tree
5. Red black Tree
'''

#1. Binary Tree:
#A Binary Tree is a Tree which contains of atmost of 2 children
'''
0 children
1 children
2 children

Representation:
            10  --->Level 0
           /  \
          20   30  ---->Level 1
         / \     \
       40  50    60   ---->Level 2
  
'''
#Binary Tree Construction:
'''class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)'''

#Tree Traversal:3 Types
'''
1. Pre-order :  Root --> Left --> Right
2. In-order : Left --> Root --> Right
3. Post-order : Left --> Right --> Root
'''
#Pre-Order:
#Algorithm:
'''
1. Check whether root node is exist or not :
   ---> If not : return Nothing
2. Traverse through root Node
3. Trvaerse Through root.left part
4. Traverse through root.right part
'''
#In-Order:
#Algorithm:
'''
1. Check whether root node is exist or not :
   ---> If not : return Nothing
2. Trvaerse Through root.left part
3. Traverse through root Node
4. Traverse through root.right part
'''
#Post-Order:
#Algorithm:
'''
1. Check whether root node is exist or not :
   ---> If not : return Nothing
2. Trvaerse Through root.left part
3. Traverse through root.right part
4. Traverse through root Node
'''
#Leet Code : 94, 144, 145, 226
class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
def preorder(root):
    if root is None:
        return 
    print(root.data, end = " -> ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data, end = " -> ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data, end = " -> ")

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
print("Pre-order Tree Traversal:")
preorder(root)
print()

print("In-order Tree Traversal:")
inorder(root)
print()

print("Post-order Tree Traversal:")
postorder(root)
print()