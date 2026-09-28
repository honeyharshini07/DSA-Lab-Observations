class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_begin(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            self.tail = new
            new.next = self.head
        else:
            new.next = self.head
            self.head = new
            self.tail.next = self.head

        print("Insertion completed")

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            self.tail = new
            new.next = self.head
        else:
            new.next = self.head
            self.tail.next = new
            self.tail = new

        print("Insertion completed")

    def insert_position(self, position, data):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insert_begin(data)
            return

        if self.head is None:
            print("Invalid position")
            return

        temp = self.head

        for i in range(position - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid position")
                return

        new = Node(data)
        new.next = temp.next
        temp.next = new

        if temp == self.tail:
            self.tail = new

        print("Insertion completed")

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            print("Deleted value =", self.head.data)
            self.head = None
            self.tail = None
        else:
            print("Deleted value =", self.head.data)
            self.head = self.head.next
            self.tail.next = self.head

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            print("Deleted value =", self.tail.data)
            self.head = None
            self.tail = None
            return

        temp = self.head

        while temp.next != self.tail:
            temp = temp.next

        print("Deleted value =", self.tail.data)

        temp.next = self.head
        self.tail = temp

    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.delete_begin()
            return

        temp = self.head

        for i in range(position - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid position")
                return

        if temp.next == self.head:
            print("Invalid position")
            return

        delete_node = temp.next

        if delete_node == self.tail:
            self.tail = temp

        temp.next = delete_node.next

        print("Deleted value =", delete_node.data)

    def count(self):
        if self.head is None:
            print("Number of nodes = 0")
            return

        c = 0
        temp = self.head

        while True:
            c += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes =", c)

cll = CircularLinkedList()
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
        cll.insert_begin(x)
    elif choice == 2:
        x = int(input("Value: "))
        cll.insert_end(x)
    elif choice == 3:
        idx = int(input("Index: "))
        x = int(input("Value: "))
        cll.insert_position(idx, x)
    elif choice == 4:
        cll.delete_begin()
    elif choice == 5:
        cll.delete_end()
    elif choice == 6:
        idx = int(input("Delete index: "))
        cll.delete_position(idx)
    elif choice == 7:
        cll.count()
    elif choice == 8:
        print("The program is exiting")
        break
    else:
        print("Enter a valid choice")
