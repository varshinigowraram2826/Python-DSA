"""class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Inorder(Root):
    if Root==None:
        return
    Inorder(Root.left)
    print(Root.data,end=" ")
    Inorder(Root.right)
    
def preorder(Root):
    if Root==None:
        return
    print(Root.data,end=" ")
    preorder(Root.left)
    preorder(Root.right)

def postorder(Root):
    if Root==None:
        return 
    preorder(Root.left)
    preorder(Root.right)
    print(Root.data,end=" ")   

Root=Node(10)
Root.left=Node(20)
Root.right=Node(30)
Root.left.left=Node(40)
Root.left.right=Node(50)
Root.right.right=Node(60)
Root.right.left=Node(70)
Inorder(Root)
print()
preorder(Root)
print() 
postorder(Root)


#searching an element in a tree O(n)
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder(Root):
    if Root==None:
        return 
    print(Root.data,end=" ")
    preorder(Root.left)
    preorder(Root.right)
k=60
def search(Root,k):
    if Root==None:
        return False
    if  Root.data==k:
        return True
    return search(Root.left,k) or search(Root.right,k)
Root=Node(50)
Root.left=Node(40)
Root.right=Node(30)
Root.left.left=Node(20)
Root.left.right=Node(50)
Root.right.right=Node(60)
Root.right.left=Node(70)
Flag=search(Root,k)
if Flag:
    print( "Element Found")
else:
    print( "Element not Found")
preorder(Root)

#to find size of tree(no.of nodes)

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def Inorder(Root):
    if Root==None:
        return    
    Inorder(Root.left)
    print(Root.data,end=" ")
    Inorder(Root.right)
def size(Root):
    if Root==None:
        return 0
    else:
        return 1+size(Root.left)+size(Root.right)         
Root=Node(10)
Root.left=Node(20)
Root.right=Node(30)
Root.left.left=Node(40)
Root.left.right=Node(50)
Root.right.right=Node(60)
Root.right.left=Node(70)        
Inorder(Root)
print()
print(size(Root))
#height of a treee
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def Inorder(Root):
    if Root==None:
        return 
    Inorder(Root.left)
    print(Root.data,end=" ")
    Inorder(Root.right)
def height(Root):
    if Root==None:
        return -1
    return max(1+height(Root.left),1+height(Root.right))
Root=Node(10)
Root.left=Node(20)
Root.right=Node(30)
Root.left.left=Node(40)
Root.left.left.left=Node(90))
Root.left.right=Node(50)
Root.right.right=Node(60)
Root.right.left=Node(70)        
Inorder(Root)
print()
print(height(Root))


#binary search tree: left<root<right
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Inorder(Root):
    if Root==None:
        return
    Inorder(Root.left)
    print(Root.data,end=" ")
    Inorder(Root.right)

def insertion(Root,data):
    if Root==None:
        return Node(data)
    if Root.data<data:
        Root.right=insertion(Root.right,data)
    else:
        Root.left=insertion(Root.left,data)
    return Root
Root=Node(70)
insertion(Root,20)
insertion(Root,30)
insertion(Root,50)
insertion(Root,39)
insertion(Root,56)
insertion(Root,99)
insertion(Root,26)
insertion(Root,12)
Inorder(Root)
"""
#searching an element in a tree using BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Inorder(Root):
    if Root==None:
        return
    Inorder(Root.left)
    print(Root.data,end=" ")
    Inorder(Root.right)
def insertion(Root,data):
    if Root==None:
        return Node(data)
    if Root.data<data:
        Root.right=insertion(Root.right,data)
    else:
        Root.left=insertion(Root.left,data)
    return Root
k=10
def search(Root,data,k):
    if Root==None:
        print("element not found")
        return
    if Root.data==k:
        print("element found")
        return
    if Root.data<k:
        search(Root.right,k)
    else:
        search(Root.left,k)
Root=Node(50)
insertion(Root,40)
insertion(Root,30)
insertion(Root,20)
insertion(Root,10)
search(Root,k)
Inorder(Root)        
"""
#deletion at a node
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def Inorder(Root):
    if Root==None:
        return
    Inorder(Root.left)
    print(Root.data,end=" ")
    Inorder(Root.right)
def insertion(Root,data):
    if Root==None:
        return Node(data)
    if Root.data<data:
        Root.right=insertion(Root.right,data)
    else:
        Root.left=insertion(Root.left,data)
    return Root
def mini(Root):
    temp=Root
    while temp.left:
        temp=temp.left
    return temp
def deletion(Root,data):
    if Root==None:
        return None
    if Root.data<data:
        Root.right=deletion(Root.right,data)
    elif Root.data>data:
        Root.left= deletion(Root.left)
    else:
        if Root.left==None:
            return Root.right
        elif Root.right==None:
            return Root.left
        successor=mini(Root.right)
        Root.data=successor.data
        Root.right=deletion(Root.right,successor.data)
    return Root
Root=Node(10)
insertion(Root,7)
insertion(Root,3)
insertion(Root,2)
insertion(Root,4)
insertion(Root,8)
insertion(Root,9)
insertion(Root,15)
insertion(Root,12)
insertion(Root,18) 
Inorder(Root)
mini(Root)   
deletion(Root,15)
print()
Inorder(Root)
