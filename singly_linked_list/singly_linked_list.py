class Node: 
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
 
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next   


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)

         #check if there is no head
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.set_next(new_node)  #if we have a head, set the tail
            self.tail = new_node

    def remove_head(self):
         #check if there is no head
         if not self.head:
             return None
        # if hed has no next, there is a single element in the linked list 
        if  not self.head.get_next():
            head = self.head
            self.head = None 
            self.tail = None

            return head.get_value()


