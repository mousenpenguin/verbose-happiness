class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None #linkedlist點
        
        
class MyHashSet:
    def MD5(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8")) 
        h = int(h.hexdigest(),16)  #轉成10進位
        return h
        
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity 
       
    
    def add(self, key):
        key = self.MD5(key)
        index = key % self.capacity 
        node = ListNode(key)
        if self.data[index] == None:
            self.data[index] = node
        else:
            c = self.data[index]
            
            if c.next == None:
                if c.val != key:
                    c.next = node
            else:
                while c.val != key and c.next != None:
                    c == c.next
                if c.val != key:
                    c.next = node
        
            
    def remove(self, key):
        key = self.MD5(key)
        index = key % self.capacity
        if self.data[index] == None: #刪掉
            return
        if self.data[index].val == key: #當他下一個存在
            self.data[index] = self.data[index].next
        else:
            current = self.data[index]
            while current.next:
                if current.next.val == key:
                    current.next = c.next.next
                else:
                    current = current.next #不是的話頭就變下一個繼續找

        
    def contains(self, key):
        key = self.MD5(key)
        index = key % self.capacity
        c = self.data[index]
        while c:
            if c.val == key:
                return True
            else:
                c = c.next
        return False