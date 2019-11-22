class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val):
    
    if self.root == root:
        self.val = val              #取代現有數值
    elif self.root > root:            #root屬於左子樹部分於
        if self.left:
            self.left.put(root,val)
        else:                       #左子樹為空
            self.left = TreeNode(root,val)
    else:                           # root屬於右子樹部分於
        if self.right:
            self.right.put(root,val)
        else:                       #右子樹為空
            self.right = TreeNode(root,val)



    def delete(root, key):
  # 要是root不存在，便返回
	if not root: 
		return root
	# 要是目標值小於root值，尋找左邊子樹
	if root.val > key: 
		root.left = delete_Node(root.left, key)
	# 要是目標值大於root值，尋找右邊子樹
	elif root.val < key: 
		root.right= delete_Node(root.right, key)
	#要是目標值=root值，刪掉節點
	else: 
	#要是沒有右子樹的話，刪掉節點，新的root點為root左節點
		if not root.right:
			return root.left
	#要是沒有左子樹的話，刪掉節，新的root點為root右節點
		if not root.left:
			return root.right
  # 如果同時存在左右兩個子節點，則將其值替換為右子樹中的最小值，然後刪掉在右邊子樹中最小節點
		temp_val = root.right
		mini_val = temp_val.val
		while temp_val.left:
			temp_val = temp_val.left
			mini_val = temp_val.val
	# 替換
		root.val = mini 
  # 刪掉在右邊子樹中最小節點
		root.right = deleteNode(root.right,root.val)
	return root



    def search(self, root, target):
 	
 	if root is None:
 		return None 
 	elif root.target == target:
 		return root		
 	elif root.target > target:
 		return self.__find(root.left, target)
 	else:
 		return self.__find(root.right, target)


 	def modify(self, root, target, new_val):
#Pass  Will see other classmates' work


#reference: https://www.youtube.com/watch?v=YlgPi75hIBc&feature=youtu.be
#https://www.laurentluce.com/posts/binary-search-tree-library-in-python/