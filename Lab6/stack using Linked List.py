class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None

    def push(self,data):
        new=Node(data)
        new.next=self.top
        self.top=new
        print(data,"pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            temp=self.top
            print(temp.data,"popped from stack")
            self.top=self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:",self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp=self.top
            print("Stack elements")
            while temp is not None:
                print(temp.data)
                temp=temp.next

s=stack()
while True:
    print("1.Push() using Linked List")
    print("2.Pop() using Linked List")
    print("3.Peek() using Linked List")
    print("4.Display() using Linked List")
    print("5.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        data=int(input("Enter the value:"))
        s.push(data)
    elif choice==2:
        s.pop()
    elif choice==3:
        s.peek()
    elif choice==4:
        s.display()
    elif choice==5:
        print("The program is exiting")
        break
    else:
        print("Enter a vaild choice")
    
