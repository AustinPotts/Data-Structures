from singly_linked_list import Node
from singly_linked_list import LinkedList
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = LinkedList()
    
    # Find length of size 
    def __len__(self):
        return self.size

    # Add to the Linked List + Size
    def enqueue(self, value):
        #access the LinkedList Head Def
        self.storage.make_new_head(value)
        self.size += 1
    
    #Remove from linked list 
    def dequeue(self):
        if self.__len__() = 0: 
            return none 
        else:
            front = self.storage.remove_from_tail()
             self.size -= 1
             return front.value
