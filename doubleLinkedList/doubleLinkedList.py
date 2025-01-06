class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        if self.length == 0:
            self.__init__(value)
            return True
        
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            new_node.next = self.head
            temp.prev = new_node
            self.head = new_node
        
        self.length += 1
        return True
    
    def popfirst(self):
        if self.length == 0:
            return False
        
        cur = self.head
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            temp = cur.next
            self.head.next = None
            temp.prev = None
            self.head = temp

        self.length -= 1
        return cur
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr


    def set_val(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        curr = self.get(index)
        curr.value = value
        return True
    

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            prev_item = self.get(index-1)
            curr = prev_item.next
            new_node = Node(value)
            prev_item.next = new_node
            new_node.prev = prev_item
            new_node.next = curr
            curr.prev = new_node
            self.length += 1
        
        return True

    def remove(self, index):
        if index < 0 or index > self.length-1:
            return False
        
        if index == 0:
            return self.popfirst()
        elif index == self.length-1:
            return self.pop()
        else:
            curr = self.get(index)
            prev_item = curr.prev
            post = curr.next
            prev_item.next = post
            post.prev = prev_item
            curr.next = None
            curr.prev = None
            return curr
