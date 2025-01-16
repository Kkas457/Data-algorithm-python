class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:
    def __init__(self, val):
        new_node = Node(val)
        self.top = new_node
        self.height = 1
    
    def push(self, val):
        if not self.top:
            self.__init__(val)
        else:
            new_node = Node(val)
            new_node.next = self.top
            self.top = new_node
            self.height += 1
        
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp