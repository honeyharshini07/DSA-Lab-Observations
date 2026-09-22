class stack:
    def _init_(self):
        self.top=None

def push(self,data):
    new=node(data)
    new.next=top
    self.top=new
    print(data,"pushed into stack")

def pop(self):
    if self.top is None:
        print("Stack underflow")
    else:
        temp=self.top
        print(temp.data,"popped from stack")
        self.top=self.top.next

def peek():

def display():
    

while true:
    print("1.Push() using Linked List")
    print("2.Pop() using Linked List")
    print("3.Peek() using Linked list")
    print("4.Display() using Linked List")
    print("5.Exit")
    choice=int(input("Enter the choice:"))
if choice==1:
    newelement=
    stack.push(newelement)
elif choice==2:
    stack.pop()
elif choice==3:
    stack.peek()
elif choice==4:
    stack.display()
elif choice==5:
    print("The program is exiting")
else:
    print("Enter a vaild choice")
