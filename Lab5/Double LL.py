class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

        print("Insertion completed")

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new
            new.prev = temp

        print("Insertion completed")

    def insert_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_begin(data)
            return

        if self.head is None:
            print("Invalid index")
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return

            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new = Node(data)

        new.next = temp.next
        new.prev = temp

        if temp.next is not None:
            temp.next.prev = new

        temp.next = new

        print("Insertion completed")

    def deleteBeg(self):
        if self.head is None:
            print("Can't perform delete operation")
            return

        temp = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("Value deleted =", temp.data)

    def deleteEnd(self):
        if self.head is None:
            print("Can't perform delete operation")
            return

        temp = self.head

        if temp.next is None:
            self.head = None
            print("Value deleted =", temp.data)
            return

        while temp.next:
            temp = temp.next

        print("Value deleted =", temp.data)

        temp.prev.next = None
        temp.prev = None

    def deleteIndex(self, index):
        if self.head is None:
            print("Can't perform delete operation")
            return

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.deleteBeg()
            return

        temp = self.head

        for i in range(index):
            if temp is None:
                print("Invalid index")
                return

            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        if temp.prev is not None:
            temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        print("Value deleted =", temp.data)

    def count(self):
        c = 0
        temp = self.head

        while temp:
            c += 1
            temp = temp.next

        print(f"Number of nodes = {c}")


dll = DoublyLinkedList()

while True:
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at index")
    print("4. Delete at first node")
    print("5. Delete at last node")
    print("6. Delete at index")
    print("7. Count number of nodes")
    print("8. Exit")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        x = int(input("Value: "))
        dll.insert_begin(x)
    elif choice == 2:
        x = int(input("Value: "))
        dll.insert_end(x)
    elif choice == 3:
        idx = int(input("Index: "))
        x = int(input("Value: "))
        dll.insert_index(idx, x)
    elif choice == 4:
        dll.deleteBeg()
    elif choice == 5:
        dll.deleteEnd()
    elif choice == 6:
        idx = int(input("Delete index: "))
        dll.deleteIndex(idx)
    elif choice == 7:
        dll.count()
    elif choice == 8:
        print("The program is exiting")
        break
    else:
        print("Enter a valid choice")
