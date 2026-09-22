def push(newelement):
    if top==-1:
        print("Overflow of stack:")
    else:
        element=stack[top]
        top=+1

def pop():
    if top==-1:
        print("Stack underflow")
    else:
        element=stack[top]
        top=-1
        print("Deleted value=",element)

def peek():

def display():
    

while true:
    print("1.Push() using Array")
    print("2.Pop() using Array")
    print("3.Peek() using Array")
    print("4.Display() using Array")
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
    
