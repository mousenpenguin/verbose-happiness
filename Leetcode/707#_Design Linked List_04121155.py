class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index):
        if self.size == 0:
            return -1
        
        elif index < 0 or index >= self.size:
            return -1
        

        pointer = self.head
        for i in range(index):
            pointer = pointer.next
        return pointer.val


    def addAtHead(self, val):
        if self.size == 0:
            self.head = Node(val)
        
        else:
            node = Node(val)
            node.next = self.head
            self.head = node
            
        self.size+=1
   
    def addAtTail(self, val):
        if self.size == 0:
            self.head = Node(val)
        
        else:
            pointer = self.head
            while pointer.next!=None:
                pointer = pointer.next
            else:
                pointer.next = Node(val)
                
        self.size+=1

    def addAtIndex(self, index, val):
        if self.size == 0:
            self.head = Node(val)
            
        else:
            if index == 0:
                self.addAtHead(val)
                
            elif index == self.size:
                self.addAtTail(val)
                
            elif index < 0 or index >self.size:
                return
            
            else:
                pointer = self.head
                for i in range(index-1):
                    pointer = pointer.next
                node = Node(val)
                node.next = pointer.next
                pointer.next = node
                
        self.size+=1
       

    def deleteAtIndex(self, index):
        if self.size == 0:
            return
        
        if index < 0 or index >= self.size:
            return
        
        else:
            pointer = self.head
            if index == 0:
                self.head = pointer.next
                
            else:
                for i in range(index-1):
                    pointer = pointer.next
                pointer.next = pointer.next.next

        self.size-=1