class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=0
def height(root):
    if root is None:
        return -1
    return root.height
def balance(root):
    if root is None:
        return 0
    return height(root.left)-height(root.right)
def right_rotate(y):
    x=y.left
    a=x.right
    x.right=y
    y.left=a
    y.height=max(height(y.left),height(y.right))+1
    x.height=max(height(x.left),height(x.right))+1
    return x
def left_rotate(x):
    y=x.right
    a=y.left
    y.left=x
    x.right=a
    x.height=max(height(x.left),height(x.right))+1
    y.height=max(height(y.left),height(y.right))+1
    return y
def insert(root,x):
    if root is None:
        return Node(x)
    if x<root.data:
        root.left=insert(root.left,x)
    elif x>root.data:
        root.right=insert(root.right,x)
    else:
        print("Duplicate values not allowed")
        return root
    root.height=max(height(root.left),height(root.right))+1
    b=balance(root)
    if b>1 and x<root.left.data:
        return right_rotate(root)
    if b<-1 and x>root.right.data:
        return left_rotate(root)
    if b>1 and x>root.left.data:
        root.left=left_rotate(root.left)
        return right_rotate(root)
    if b<-1 and x<root.right.data:
        root.right=right_rotate(root.right)
        return left_rotate(root)
    return root
def min_value(root):
    while root.left:
        root=root.left
    return root
def delete(root,key):
    if root is None:
        return root
    if key<root.data:
        root.left=delete(root.left,key)
    elif key>root.data:
        root.right=delete(root.right,key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp=min_value(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    root.height=max(height(root.left),height(root.right))+1
    b=balance(root)
    if b>1 and balance(root.left)>=0:
        return right_rotate(root)
    if b>1 and balance(root.left)<0:
        root.left=left_rotate(root.left)
        return right_rotate(root)
    if b<-1 and balance(root.right)<=0:
        return left_rotate(root)
    if b<-1 and balance(root.right)>0:
        root.right=right_rotate(root.right)
        return left_rotate(root)
    return root
def search(root,key):
    if root is None or root.data==key:
        return root
    if key<root.data:
        return search(root.left,key)
    return search(root.right,key)
def levelorder(root):
    if root is None:
        print("Tree is empty")
        return
    q=[root]
    while q:
        n=q.pop(0)
        print(n.data,end=" ")
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
root = None
while True:
    print("1.Insert")
    print("2.Delete")
    print("3.Search")
    print("4.Levelorder")
    print("5.Exit")
    ch = int(input("Enter your choice: "))
    if ch==1:
        x=int(input("Enter value: "))
        root=insert(root,x)
        print("Value is inserted")
    elif ch==2:
        x=int(input("Enter value: "))
        if search(root,x):
            root=delete(root,x)
            print("Node deleted")
        else:
            print("Value not found")
    elif ch==3:
        x=int(input("Enter value: "))
        if search(root, x):
            print("Found")
        else:
            print("Not Found")
    elif ch==4:
        levelorder(root)
        print()
    elif ch==5:
        print("The program is being terminated.")
        break
    else:
        print("Invalid choice")
