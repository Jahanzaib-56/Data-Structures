# Node class
class Node:

    # Node constructor  
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():

    # LinkedList constructor
    def __init__(self):
        self.head = None
        self.c = 0

    # Returns the length of the LinkedList
    def __len__(self):
        return self.c
    
    # Returns the string representation of the LinkedList
    def __str__(self):

        curr = self.head
        result = ''

        while curr != None:
            result = result + str(curr.data) + ' -> '
            curr = curr.next

        return result[:-3]
    
    # Returns the value at the given index
    def __getitem__(self, index):

        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1

        return 'IndexError'
    
    # Insert a node at the head of the LinkedList
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.c += 1

    # Insert a node at the end of the LinkedList
    def append(self, value):

        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.c = self.c + 1
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self.c = self.c + 1

    # Insert a node after a given node
    def insert(self, after, value):

        newNode = Node(value)
        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            newNode.next = curr.next
            curr.next = newNode
            self.c = self.c + 1
        else:
            print("Item not found: Can't insert after it")

    # Clear the LinkedList
    def clear(self):
        self.head = None
        self.c = 0

    # Delete the head of the LinkedList
    def delete_head(self):

        if self.head == None:
            print("List is Empty")

        self.head = self.head.next
        self.c -= 1

    # Delete the last node of the LinkedList
    def pop(self):

        if self.head == None:
            print('Empty List')

        curr = self.head

        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.c = self.c - 1

    # Remove a node with a given value
    def remove(self, value):

        if self.head == None:
            print("Empty List")

        if self.head.data == value:
            return self.delete_head()

        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            print('Item not found')
        else:
            curr.next = curr.next.next
            self.c -= 1

    # Search for a node with a given value
    def search(self, item):

        curr = self.head
        index = 0

        while curr != None:
            if curr.data == item:
                return index
            curr = curr.next
            index += 1

        return "Item not found"
    
    # Replace the maximum node with a given value
    def replace_max(self, val):

        temp = self.head
        max = temp

        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next

        max.data = val

    # Reverse the LinkedList
    def reverse(self):

        prev_node = None
        curr_node = self.head

        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

Mylist = LinkedList()

Mylist.append(10)
Mylist.append(20)
Mylist.append(30)
Mylist.insert(20, 25)
Mylist.remove(10)
Mylist.reverse()
print(Mylist)
print(Mylist.search(20))
Mylist.replace_max(100)
print(Mylist)
Mylist.clear()
print(Mylist)   
