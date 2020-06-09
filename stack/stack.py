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
class Stack:
     def __init__(self):
         self.size = 0
         # self.storage = ?
         self.storage = list()

     def __len__(self):
         pass
         self.size = len(self.storage)
         return self.size

     def push(self, value):
         pass
         self.storage.append(value)

     def pop(self):
         pass
         if self.storage.__len__() is 0:
             return None
         else:
             top = self.storage.pop(-1)
             return top