
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack? A: Linked List can have values added anywhere through the list while an array you cannot

   - Array is a collection of elements of similar data type.
   - Linked List is an ordered collection of elements of same type, which are connected to each other using pointers.

"""

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value 
        self.next_node = next_node

    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    def add_to_tail(self,value):
        new_node = Node(value, None)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def make_new_head(self,value):
        new_node = Node(value)
        previous_head = self.head
        self.head = new_node
        self.head.set_next(previous_head)

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next:
            head = self.head
            self.head = None
            self.tail = None 
            return head.get_value()
        
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None 
            self.tail = None 
            return value
        current = self.head
        while current.get_next() != self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value
        
    def contains(self,value):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        return max_value



class Stack:
     def __init__(self):
         self.size = 0
         # self.storage = ?
         self.storage = LinkedList()

     # Check size of the stack
     def __len__(self):
         pass
         self.size = len(self.storage)
         return self.size
     
     # Push to stack by appending 
     def push(self, value):
         pass
         self.storage.add_to_tail(value)

     def pop(self):
         pass
         if len(self.storage) is 0:
             return None
         else:
             top = self.storage.remove_tail()
             return top.value