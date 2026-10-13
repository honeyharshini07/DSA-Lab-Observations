class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,x):
    if root is None:
        return Node(x)
        if x<root.data:
            root.left=insert(root,left,x)
        elif x>root.data:
            root.right=insert(root,right,x)
        else:
            print("Duplicate value is not allowed")
        return root
def Preorder(root):
    if root is None:
        return
    print(root.data,end="")
    Preorder(root.left)
    Preorder(root.right)
def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.data,end="")
    Inorder(root.right)
def Postorder(root):
    if root is None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.data,end="")
def find_min(root):
    if root is None:
        return None
    while root.left is not None:
        root=root.left
    return root
def find_max(root):
    if root is None:
        return None
    while root.right is not None:
        root=root.right
    return root
def search(root,data):
    if root is None:
        return None
    if data<root.data:
        return search(root.left,data)
    elif data>root.data:
        return search(root.right,data)
    else:
        return root
def count_nodes(root):
    if root is None:
        return 0
    else:
        return count_nodes(root.left)+count_nodes(root.right)+1
def count_leaf(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return count_leaves(root.left)+count_leaves(root.right)
def count_internal(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 0
    else:
        return count_internals(root.left)+count_intervnals(root.right)+1
def height(root):
    if root is None:
        return -1
    left_height=height(root.left)
    right_height=height(root.right)
    return max(left_height,right_height)+1
def delete(root,x):
    if root is None:
        return None
    elif x<root.data:
        root.left=delete(root.left,x)
    elif x>root.data:
        root.right=delete(root.right,x)
    else:
        #No children
        if root.left is None and root.right is None:
            root=None
        #One left child
        elif root.right is None:
            root=root.left
        #One right child
        elif root.left is None:
            root=root.right
        #Two childres of a node
        else:
            successor=find_min(root.right)
            root.data=successor.data
            root.right=delete(root.right,successor.data)
        return root
def display(root,level):
    if root is None:
        return
    elif level==0:
        print(root.data,end="")
    else:
        print(root.left,level-1)
        print(root.right,level-1)
def level_order(root):
    h=height(root)
    for level in range(h):
        display(root,level)

#Menu-driven Program
root=None
while True:
    print("1.Insert")
    print("2.Pre-Order Traversal")
    print("3.In-Order Traversal")
    print("4.Post-Order Traversal")
    print("5.Find Minimum")
    print("6.Find the Maximum")
    print("7.Search")
    print("8.Delete")
    print("9.Count no of nodes")
    print("10.Count no of leaves")
    print("11.Count no of internal nodes")
    print("12.Height of tree")
    print("13.Level-order Traversal")
    print("14.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        data=int(input("Enter the data to be inserted:"))
        root=insert(root,data)
        print("Element inserted successfully")
    elif choice==2:
        print("Preorder Traversal:",end="")
        if root is None:
            print("Tree is Empty")
        else:
            Preorder(root)
            print()
    elif choice==3:
        print("Inorder Traversal:",end="")
        if root is None:
            print("Tree is Empty")
        else:
            Inorder(root)
            print()
    elif choice==4:
        print("Postorder Traversal:",end="")
        if root is None:
            print("Tree is Empty")
        else:
            Postorder(root)
            print()
    elif choice==5:
        node=find_min(root)
        if node is None:
            print("Tree is Empty")
        else:
            print("Minimum element:",node.data)
    elif choice==6:
        node=find_max(root)
        if node is None:
            print("Tree is Empty")
        else:
            print("Maximum element:",node.data)
    elif choice==7:
        data=int(input("Enter the data to be searched:"))
        node=search(root,data)
        if node is None:
            print("Element",data,"is not found")
        else:
            print("Element",data,"is found")
    elif choice==8:
        data=int(input("Enter the data to be deleted:"))
        root=delete(root,data)
    elif choice==9:
        print("Number of nodes:",count_nodes)
    elif choice==10:
        print("Number of leaf nodes:",count_leaf)
    elif choice==11:
        print("Number of internal nodes:",count_internal)
    elif choice==12:
        print("Height of BST:",height(root))
    elif choice==13:
        print("Level order Traversal:",end="")
        if root is None:
            print("Tree is Empty")
        else:
            level_order(root)
            print()
    elif choice==14:
        print("Program terminated.")
        break
    else:
        print("Enter a valid choice.")
























    
