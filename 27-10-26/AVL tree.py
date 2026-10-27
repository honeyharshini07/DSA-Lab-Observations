class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def height(root):
    if root is None:
        return -1
    return root.height
def balance(root):
    if root is None:
        return 0
    return height(root.left)-height(root)
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
            root.left=insert(root,left,x)
        elif x>root.data:
            root.right=insert(root,right,x)
        else:
            print("Duplicate valie s not allowed")
        return root
    root.height = max(get_height(root.left),
                      get_height(root.right)) + 1

    balance = get_balance(root)

    # LL Case
    if balance > 1 and x < root.left.data:
        return right_rotate(root)

    # RR Case
    if balance < -1 and x > root.right.data:
        return left_rotate(root)

    # LR Case
    if balance > 1 and x > root.left.data:
        root.left = left_rotate(root.left)
    # RL Case
    if balance < -1 and x < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
