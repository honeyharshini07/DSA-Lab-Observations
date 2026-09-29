class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def PreOrderTraversal(node):
    if node is None:
        return
    else:
         print(node.data,end=",")
         PreOrderTraversal(node.left)
         PreOrderTraversal(node.right)
def InOrderTraversal(node):
    if node is None:
        return
    else:
        InOrderTraversal(node.left)
        print(node.data,end=",")
        InOrderTraversal(node.right)
def PostOrderTraversal(node):
    if node is None:
        return
    else:
        PostOrderTraversal(node.left)
        PostOrderTraversal(node.right)
        print(node.data,end=",")
def LevelOrderTraversal(node):
    if node is None:
        return
    else:
        print(node.data,end=",")
        i=0
        while True:
            if i<10:
                if i%2==0:
                    LevelOrderTraversal(node.left)
                    i=i+1
                    return
                else:
                    LevelOrderTraversal(node.right)
                    i=i+1
            return
root=Node('A')
nodeB=Node('B')
nodeC=Node('C')
nodeD=Node('D')
nodeE=Node('E')
nodeF=Node('F')
nodeG=Node('G')
nodeH=Node('H')
nodeI=Node('I')

root.left=nodeB
root.right=nodeC
nodeB.left=nodeD
nodeB.right=nodeE
nodeC.right=nodeG
nodeC.left=nodeF
nodeD.left=nodeH
nodeD.right=nodeI
print("The pre-order traversal of the binary tree is:")
PreOrderTraversal(root)
print("\nThe in-order traversal of the binary tree is:")
InOrderTraversal(root)
print("\nThe post-order traversal of the binary tree is:")
PostOrderTraversal(root)
print("\nThe level-order traversal of the binary tree is:")
LevelOrderTraversal(root)
