'''
class stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "stack is empty"
    def is_empty(self):
        return len(self.items) == 0
s = stack()
s.push(10)
s.push(20)
s.push(30)
print(s.items)
print(s.pop())
print(s.peek())
print(s.is_empty())

#stack using linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        new_node=node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if not self.is_empty():
            val = self.top.data
            self.top = self.top.next
            return val
        return "stack is Empty"
    def peak(self):
        if not self.is_empty():
            val = self.top.data
            return val
        return "stack is empty"
        
        
    def is_empty(self):
        return self.top is None
    def traverse(self):
        elements = []
        curr = self.top
        while curr :
            elements.append(curr.data)
            curr = curr.next
        return elements
s = stack()
s.push(10)
s.push(20)
s.push(30)

class queue:
    def __init__(self):
        self.items = []
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "queue is empty" 
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "queue is empty"
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
s = queue()
s.enqueue(10)
s.enqueue(20)   
s.enqueue(30)
print(s.items)
print(s.dequeue())
print(s.peek())     
print(s.size())
'''
class circular_queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    def enqueue(self, data):
        if self.is_full():
            return "Queue is full"
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val
    def display(self):
        if self.is_empty():
            return "Queue is empty"
        res= []
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            res.append(self.queue[index])
        return res