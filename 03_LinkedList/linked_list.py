class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initialize next as None

# Function to insert a node at the end of the linked list
def insert_end(head, n):
    if head is None:
        head = Node(n)  # Create a new node if the list is empty
        return head
    else:
        temp = head
        while temp:  # Traverse to the end of the list
            prev = temp
            temp = temp.next
        newnode = Node(n)
        prev.next = newnode  # Link the last node to the new node
        return head

# Function to display the linked list elements
def display(head):
    temp = head
    if temp is None:
        print("Empty List")
        return
    while temp:
        print(temp.data)  # Print each node's data
        temp = temp.next

# Function to insert a node at the beginning of the linked list
def insert_first(head, n):
    temp = head
    newnode = Node(n)
    newnode.next = temp  # Point new node to the current head
    head = newnode  # Update head to the new node
    return head

# Function to count the number of nodes in the linked list
def count(head):
    temp = head
    c = 0
    if temp is None:
        print("Empty List")
        return c
    while temp:
        c += 1  # Increment count for each node
        temp = temp.next
    return c

# Function to search for a node in the linked list
def search(head, n):
    temp = head
    pos = 0
    if temp is None:
        print("Empty List")
        return 0
    while temp:
        pos += 1
        if temp.data == n:
            return pos  # Return position if found
        temp = temp.next
    return -1  # Return -1 if not found

# Function to delete a node with a given value
def deletion(head, n):
    temp = head
    if temp is None:
        print("Empty List")
        return head
    elif temp.data == n:  # If the node to be deleted is the head
        print("Deleted item:", temp.data)
        head = temp.next
        return head
    else:
        prev = temp
        temp = temp.next
        while temp:
            if temp.data == n:
                prev.next = temp.next # Remove the node from the list
                print("Deleted item:", temp.data)
                return head
            prev = temp
            temp = temp.next
        print("Item Not found")
        return head

# Main Menu for Linked List Operations
head = None
while True:
    print("**** Main Menu ****")
    print("1. INSERT END")
    print("2. DISPLAY")
    print("3. INSERT FIRST")
    print("4. Count")
    print("5. Search")
    print("6. Deletion")
    print("0. EXIT")
    
    ch = int(input("Enter Your Choice: "))
    
    if ch == 1:
        n = int(input("Enter data: "))
        head = insert_end(head, n)
    elif ch == 2:
        display(head)
    elif ch == 3:
        n = int(input("Enter data: "))
        head = insert_first(head, n)
    elif ch == 4:
        n = count(head)
        if n > 0:
            print("No. of elements =", n)
    elif ch == 5:
        n = int(input("Enter data which you want: "))
        pos = search(head, n)
        if pos > 0:
            print("Item is in", pos, "th position")
        else:
            print("Item not found")
    elif ch == 6:
        n = int(input("Enter data which you want to delete: "))
        head = deletion(head, n)
    elif ch == 0:
        break  # Exit the program
    else:
        print("Wrong Input")
