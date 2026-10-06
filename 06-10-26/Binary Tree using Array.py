class BinaryTreeArray:
    def __init__(self,size):
        self.tree=[None]*size
        self.size=size
#insert root
    def set_root(self,data):
        self.tree[0]=data
#set left child
    def set_left(self,parent_index,data):
        child_index=2*parent_index+1
        if child_index<self.size:
            self.tree[child_index]=data
        else:
            print("Index out of range")
#set right child
    def set_right(self,parent_index,data):
        child_index=2*parent_index+2
        if child_index<self.size:
            self.tree[child_index]=data
        else:
            print("Index out of range")
#preorder Traversal
    def preorder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        print(self.tree[index],end="")
        self.preorder(2*index+1)
        self.preorder(2*index+2)
#inorder Traversal
    def inorder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        self.inorder(2*index+1)
        print(self.tree[index],end="")
        self.inorder(2*index+2)
#postorder Traversal
    def postorder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        self.postorder(2*index+1)
        self.postorder(2*index+2)
        print(self.tree[index],end="")
#levelorder Traversal
    def levelorder(self):
        for value in self.tree:
            if value is not None:
                print(value,end="")
#display Array
    def display(self):
        for i in range(self.size):
            print(f"Index{i}:{self.tree[i]}")

tree=BinaryTreeArray(15)
tree.set_root("A")
tree.set_left(0,'B')
tree.set_right(0,'C')
tree.set_left(1,'D')
tree.set_right(1,'E')
tree.set_right(2,'F')
tree.set_right(4,'G')
tree.set_left(6,'H')
tree.set_right(6,'I')
print("Array Representation:")
tree.display()
print("PreOrder:",end="")
tree.preorder()
print("\nInOrder:",end="")
tree.inorder()
print("\nPostOrder:",end="")
tree.postorder()
print("\nLevelOrder:",end="")
tree.levelorder()
