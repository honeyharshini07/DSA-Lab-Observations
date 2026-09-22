def insert_begin(self,data):
    new=node(data)
    new.next=self.head
    self.head=new

def insert_end(self,data):
    new=node(data)
    if self.head is None:
        self.head=new
    else:
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new

def insert_index(self,index,data):
    if index==0:
        self.insert_begin(data)
        return
    elif index>self.count():
        print("Invalid index")
        return
    new=node(data)
    temp=self.head
    for i in range(index-1):
        temp=temp.next
    new.next=temp.next
    temp.next=new

def delete_Beg(self):
    if self.head is None:
        print("No data to delete")
    else:
        temp=self.head
        self.head=temp.next
        print("Deleted value=",temp.data)

def delete_End(self):
    if self.head is None:
        print("No data to delete")
    elif self.head.next is None:
        self.head=None
    else:
        temp=self.head
        temp1=temp
        while temp.next:
            temp1=temp
            temp=temp.next
            temp1.next=none

def delete(self,value):
    if self.head is None:
        printf("No data to delete")
    else:
        temp=self.head
        if temp and temp.data=value:
            self.head=temp.next
            print("Value deleted")
            return
    while temp.next and temp.next.data!=value:
        temp=temp.next
    if temp.next is None:
        print("Value not present")
    else:
        temp.next=temp.next.next
        print("Value is deleted")

def display(self):
    if self.head is None:
        print("No data")
    else:
        temp=self.head
    while temp:
        print(temp.data,end="")
        temp=temp.next
    print("None")

def count(self):
    if self.head is None:
        print("No linked List")
    else:
        c=0
        temp=self.head
        while temp:
            c=+1
            temp=temp.next
        print(f"Number of nodes={c}")

while true:
    print("1.Insert at beginning using Single Linked List")
    print("2.Insert at end using Single Linked List")
    print("3.Insert at index using Single Linked List")
    print("4.Delete at first node using Single Linked List")
    print("5.Delete at last node using Single Linked List")
    print("6.Delete by value using Single Linked List")
    print("7.Display using Single Linked List")
    print("8.Count number of nodes using Single Linked List")
    print("9.Exit")
    choice=int(input("Enter the choice:"))
if choice==1:
    newelement=
    list.insert_begin()
elif choice==2:
    list.insert_end()
elif choice==3:
    list.insert_index()
elif choice==4:
    list.delete_beg()
elif choice==5:
    list.delete_end()
elif choice==6:
    list.delete()
elif choice==7:
    list.display()
elif choice==8:
    list.count()
elif choice==9:
    print("The program is exiting")
else:
    print("Enter a vaild choice")



























    
    
