class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0
    
    def reverse(self):
        
    def reverse_between(self, x, y):
        if x < 0 or y >= self.length or x >= self.length or x > y:
            return None
        
        if x == 0 and y == self.length-1:
            return self.reverse()
        elif x > 0 and y == self.length-1:
            #find node at x-1, detach it, then reverse x to y, x-1 next = y
            temp = self.head
            for _ in range(x-1):
                temp = temp.next
            
            x_temp = temp.next
            temp.next = None
            reverse(x_temp)
            temp.next = y_temp
        elif x==0 and y < self.length-1:
            #find node at y+1, detach it, then reverse x to y, x next = y+1
            temp = self.head
            for _ in range(y):
                temp = temp.next
            
            y_temp = temp.next
            temp.next = None
            
        else:
            #find node ate x-1, y+1; detach them, then reverse x to y, x-1 next = y, x next = y +1
            
        
        


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
