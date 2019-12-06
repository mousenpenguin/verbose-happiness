from Crypto.Hash import MD5
class ListNode:
	def_init_(self, val):
		self.val = val
		self.next = None  #linkedlist點

Class HashTable:

	def_init_(self, capacity=5): #設定為五欄
		self.capacity = capacity
		self.data = [None] * capacity

	def add(self, key:str) -> None:
		h_code = MD5.new()
		h_code.update(key.encode("utf-8"))
		key = int(h_code.hexdigest(), 16) #轉成10進位

		index = key % self.capacity
		node = self.data[index]
		while node:
			if node.val == key:
				return
			node = node.next  #第一個變成下一個
		new_node = ListNode(key)
		new_node.next = self.data[index]
		self.data[index] = new node 

	def remove(self, key:str) -> None:
		h_code = MD5.new()
		h_code.update(key.encode("utf-8"))
		key = int(h_code.hexdigest(), 16) #轉成10進位

		index = key% self.capacity
		node = self.data[index]
		if node and node.val == key:
			self.data[index] = node.next
			return
		pre = None #刪掉
		while node:
			if node.val == key: #當他下一個存在
				pre.next = node.next
				return
			pre = node
			node = node.next #不是的話頭就變下一個繼續找  

	def contains(self, key:str) -> bool:
		h_code = MD5.new()
		h_code.update(key.encode("utf-8"))
		key = int(h_code.hexdigest(), 16) #轉成10進位

		index = key % self.capacity
		node = self.data[index]
		while node:
			if node.val == key:
				return True
			node = node.next
		return False  #如果下一個還找不到就會傳false


#reference: Teacher's PPT
#https://codereview.stackexchange.com/questions/118110/python-hash-table-implementation
#https://www.quora.com/How-do-I-create-my-own-hash-table-implementation-in-Python
#http://linebylinecode.com/2017/11/24/how-to-implement-a-hash-table-in-python
            
