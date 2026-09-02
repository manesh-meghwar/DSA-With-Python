# Every Binary Search Tree (BST) is a Binary Tree, but not every Binary Tree is a Binary Search Tree. A BST is simply a specific subtype of a Binary Tree that enforces a strict sorting rule.


"""
Feature	            Binary Tree	                                                Binary Search Tree (BST)
Value Ordering	    No constraints.	                                            Strict: Left < Parent < Right.
Search Speed	    O(n) - must check all nodes.	                            Average O(log n), worst O(n) if unbalanced.
Insertion Speed	    O(1) (insert anywhere) or O(n) (searching for a specific leaf).	Average O(log n), worst O(n).
In-order Traversal	Produces random order.	                                    Produces sorted order.
Primary Purpose	    Representing hierarchies and structure.	                    Fast data retrieval and sorting.
Relationship	    The parent category.	                                    A specific child/subtype of Binary Tree.


In-Order (Left → Root → Right):     Visits nodes in strictly ascending sorted order.
Pre-Order (Root → Left → Right):    Useful for making a copy of the tree.
Post-Order (Left → Right → Root):   Useful for deleting the whole tree or calculating folder sizes.
"""

class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item  = item
        self.left  = left
        self.right = right
        
        
class BST:
    
    def __init__(self):
        self.root = None
        
    # Make a insert method (in recurve style) here...!
    def insert(self, data):
        self.root = self.recursive_insert(self.root, data)


    def recursive_insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:                                    # if data less then root then insert in left-side
            root.left = self.recursive_insert(root.left, data)
        elif data > root.item:                                  # if data greater then root then insert in right-side 
            root.right = self.recursive_insert(root.right, data)
            
        return root
    
    # Make a search method here
    def search(self,data):
        return self.recurve_search(self.root, data)
    
    def recurve_search(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:                                     # if data less then root then search in left-side       
            return self.recurve_search(root.left, data)
        else:                                                    # if data less then root then search in right-side 
            return self.recurve_search(root.right, data)
        
        
    # Make a In-order traverse method here (in recursive)
    def inorder(self):
        result =[]
        self.recurve_inorder(self.root, result)
        return result
    
    
    def recurve_inorder(self,root,result):
        if root is not None:
            self.recurve_inorder(root.left, result)
            result.append(root.item)
            self.recurve_inorder(root.right,result)
            
            
    # Make a Pre-order traverse method here (in recursive)
    def preorder(self):
        result =[]
        self.recurve_preorder(self.root, result)
        return result
    
    
    def recurve_preorder(self,root,result):
        if root is not None:            
            result.append(root.item)
            self.recurve_preorder(root.left, result)
            self.recurve_preorder(root.right,result)
            
            
    
    # Make a Post-order traverse method here (in recursive)
    def postorder(self):
        result =[]
        self.recurve_postorder(self.root, result)
        return result
    
    
    def recurve_postorder(self,root,result):
        if root is not None:            
            self.recurve_postorder(root.left, result)
            self.recurve_postorder(root.right,result)
            result.append(root.item)
    
    
    # Make a method to find a minimum value
    def min_value(self,temp):
        current = temp
        while current.left is not None:                 # We have to find the min value so min value alway in left-side in BST
            current = current.left
        return current.item
    
    
    # Make a method to find a max value
    def max_value(self,temp):
        current = temp
        while current.right is not None:                # We have to find the max value so min value alway in right-side in BST
            current = current.right
        return current.item
    
    
    # Make a method to delete an element from BST
    def delete(self,data):
        self.root = self.recursive_delete(self.root,data)
    
    def recursive_delete(self,root,data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.recursive_delete(root.left,data)
        elif data > root.item:
            root.right =self.recursive_delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            root.item = self.min_value(root.right) # OR root.item = self.max_value(root.left)
            self.recursive_delete(root.right, data)    
        
        return root
    
    def size(self):
        return len(self.inorder())
            
    
    
    
            
# Quick interactive test - paste this at the bottom
if __name__ == "__main__":
    bst = BST()
    
    # Insert some values
    for num in [10, 5, 15, 3, 7, 12, 18]:
        bst.insert(num)
    
    print()
    print("*********"*10)
    
    print("Inorder (sorted):", bst.inorder())      # [3, 5, 7, 10, 12, 15, 18]
    print("Preorder:", bst.preorder())             # [10, 5, 3, 7, 15, 12, 18]
    print("Postorder:", bst.postorder())           # [3, 7, 5, 12, 18, 15, 10]
    print("Min:", bst.min_value(bst.root))         # 3
    print("Max:", bst.max_value(bst.root))         # 18
    print("Size:", bst.size())                     # 7
    print("Search 7:", bst.search(7).item)         # 7 (or None if not found)
    
    bst.delete(10)  # Delete root with two children
    print("After deleting 10:", bst.inorder())     # [3, 5, 7, 12, 15, 18]
    
    
    print()
    print("*********"*10)