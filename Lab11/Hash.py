def insert(heap,value):
    heap.append(value)
    i=len(heap)-1
    while i>0:
        parent=(i-1)//2
        if heap[i]>heap[parent]:
            heap[i],heap[parent]=heap[parent],heap[i]
            i=parent
        else:
            break
def delete(heap):
    if len(heap)==0:
        print("Heap is empty")
        return
    print("Deleted element:",heap[0])
    heap[0]=heap[-1]
    heap.pop()
    n=len(heap)
    i=0
    #Move the root downward
    while True:
        largest=i
        left=2*i+1
        right=2*i+2
        if left<n and heap[left]>heap[largest]:
            largest=left
        if right<n and heap[right]>heap[largest]:
            largest=right
        if largest!=i:
            heap[i],heap[largest]=heap[largest],heap[i]
            i=largest
        else:
            break
def display(heap):
    if len(heap)==0:
        print("Heap is empty")
    else:
        print("Heap elements:",heap)
size=10
# Separate Chaining
def chaining():
    table=[[] for i in range(size)]
    n=int(input("Enter number of elements: "))
    for i in range(n):
        x=int(input("Enter value: "))
        index=x%size
        table[index].append(x)
    print("Hash Table:")
    for i in range(size):
        print(i,":",table[i])
# Linear Probing
def linear():
    table=[-1]*size
    n=int(input("Enter number of elements: "))
    if n>size:
        print("Hash table is full")
        return
    for i in range(n):
        x=int(input("Enter value: "))
        index=x%size
        count=0
        while table[index]!=-1:
            index=(index+1)%size
        count+=1
        if count==size:
            print("Hash table is full")
            return
        table[index]=x
    print("Hash Table:")
    for i in range(size):
        print(i,":",table[i])
# Quadratic Probing
def quadratic():
    table=[-1]*size
    n=int(input("Enter number of elements: "))
    for i in range(n):
        x=int(input("Enter value: "))
        index=x%size
        j=0
        while j<size and table[(index+j*j)%size]!=-1:
            j+=1
        if j==size:
            print("No empty slot found")
            return
        table[(index+j*j)%size]=x
    print("Hash Table:")
    for i in range(size):
        print(i,":",table[i])
# Menu
heap=[]
while True:
    print("1.Insert")
    print("2.Delete")
    print("3.Display")
    print("4. Separate Chaining")
    print("5. Linear Probing")
    print("6. Quadratic Probing")
    print("7. Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        value=int(input("Enter value to insert:"))
        insert(heap,value)
        print("Value inserted")
    elif ch==2:
        delete(heap)
    elif ch==3:
        display(heap)
    elif ch==4:
        chaining()
    elif ch==5:
        linear()
    elif ch==6:
        quadratic()
    elif ch==7:
        print("Program is terminating")
        break
    else:
        print("Invalid choice")
