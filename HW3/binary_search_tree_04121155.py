class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val):
    
    if self.root == root:
        self.val = val              
    elif self.root > root:            
        if self.left:
            self.left.put(root,val)
        else:                    
            self.left = TreeNode(root,val)
    else:                           
        if self.right:
            self.right.put(root,val)
        else:                       
            self.right = TreeNode(root,val)



    def delete(root, key):

	if not root: 
		return root

	if root.val > key: 
		root.left = delete_Node(root.left, key)

	elif root.val < key: 
		root.right= delete_Node(root.right, key)

	else: 

		if not root.right:
			return root.left
	
		if not root.left:
			return root.right
  
		temp_val = root.right
		mini_val = temp_val.val
		while temp_val.left:
			temp_val = temp_val.left
			mini_val = temp_val.val

		root.val = mini 
 
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



#reference: https://www.youtube.com/watch?v=YlgPi75hIBc&feature=youtu.be
#https://www.laurentluce.com/posts/binary-search-tree-library-in-python/