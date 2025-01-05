class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
    
    def read(self):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return True
    
    def pop(self):
        if self.lenght == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next != None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.lenght -= 1
            if self.lenght == 0:
                self.head = None
                self.tail = None
            return temp
        

    def preappend(self, value):
        new_head = Node(value)
        if self.lenght == 0:
            new_head.next = self.head
            self.head = new_head
        else:
            temp = self.head
            self.head = new_head
            self.head.next = temp
        
        self.lenght +=1
        return True
    
    def pop_left(self):
        if self.lenght == 0:
            return None
        
        res = self.head
        self.head = self.head.next
        res.next = None
        self.lenght -= 1
        if self.lenght == 0:
            self.tail = None
        return res
    
    def get(self, index):
        if index-1>self.lenght or index<0:
            return None
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.lenght:
            return False
        
        if index == self.length:
            self.append(value)
            return True
        elif index == 0:
            self.preappend(value)
            return True
        else:
            pre = self.get(index-1)
            new_node = Node(value)
            new_node.next = pre.next
            pre.next = new_node
            self.lenght += 1
            return True
    
    def remove(self, index):
        if index < 0 or index > self.lenght:
            return False
        
        if index == self.length:
            self.pop()
            return True
        elif index == 0:
            self.pop_left()
            return True
        
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.lenght -= 1
        return temp
    
    def reverse(self):
        
        temp = self.head
        self.head = self.tail
        self.tail = temp

        prev = None
        curr = temp.next

        while curr:
            curr = temp.next
            curr.next = prev
            prev = curr
            curr = temp

        return self.head
    
    def get_middle_node(self):
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


my_liked_list = LinkedList(1)
my_liked_list.append(2)
my_liked_list.read()