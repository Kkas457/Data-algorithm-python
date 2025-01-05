class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return True


    def partition_list(self, x):
        l1 = LinkedList()
        dummy1 = Node()
        dummy2 = Node()
        n = 0
        while n < self.length:
            if self.head.value < x and dummy1.value == None:
                prev1 = Node(self.head.value)
                dummy1.next = prev1
            elif self.head.value < x and dummy1.value != None:
                temp = Node(self.head.value)
                prev1.next = temp
                prev1 = prev1.next
            elif self.head.value >= x and dummy2.value == None:
                prev1 = Node(self.head.value)
                dummy1.next = prev1
            elif self.head.value >= x and dummy2.value != None:
                temp = Node(self.head.value)
                prev1.next = temp
                prev1 = prev1.next

            n+=1
            self.head = self.head.next
        
        prev1.next = dummy2.next
        l1.head = dummy1.next

        return l1
#   +===================================================+
#   |               WRITE YOUR CODE HERE                |
#   | Description:                                      |
#   | - This method partitions a linked list around a   |
#   |   value `x`.                                      |
#   | - It rearranges the nodes so that all nodes less  |
#   |   than `x` come before all nodes greater or equal |
#   |   to `x`.                                         |
#   |                                                   |
#   | Tips:                                             |
#   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
#   |   to build two separate lists: one for elements   |
#   |   smaller than `x` and one for elements greater   |
#   |   or equal to `x`.                                |
#   | - `prev1` and `prev2` help us keep track of the   |
#   |   last nodes in these lists.                      |
#   | - Finally, we merge these two lists by setting    |
#   |   `prev1.next = dummy2.next`.                     |
#   | - The head of the resulting list becomes          |
#   |   `dummy1.next`.                                  |
#   +===================================================+

        
def find_kth_from_end(my_linked_list, k):
    slow = my_linked_list.head
    fast = my_linked_list.head
    for _ in range(k):
        if fast:
            fast = fast.next
        else:
            return None
    
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

