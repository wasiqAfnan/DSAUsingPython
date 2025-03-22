class Node:
    """Class to represent a node in a linked list"""
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node

def insert_end(head, n):
    """Function to insert a node at the end of the linked list"""
    if head is None:  
        return Node(n)  # If list is empty, create a new node and return
    
    temp = head
    while temp.next:  # Traverse till the last node
        temp = temp.next
    
    temp.next = Node(n)  # Add new node at the end
    return head

def display(head):
    """Function to display the linked list elements"""
    if head is None:
        print("Empty List")  # Handle empty list case
        return
    
    temp = head
    while temp:
        print(temp.data, end=" -> ")  # Print data with arrows
        temp = temp.next
    print("None")  # Indicate end of the list

def insert_first(head, n):
    """Function to insert a node at the beginning of the linked list"""
    newnode = Node(n)
    newnode.next = head  # Point new node to current head
    return newnode  # Return new node as the new head

def count(head):
    """Function to count the number of nodes in the linked list"""
    temp = head
    c = 0
    while temp:
        c += 1  # Increase count for each node
        temp = temp.next
    return c

def search(head, n):
    """Function to search for a node in the linked list"""
    temp = head
    pos = 1  # Position starts from 1
    while temp:
        if temp.data == n:
            return pos  # Return position if found
        temp = temp.next
        pos += 1
    return -1  # Return -1 if not found

def deletion(head, n):
    """Function to delete a node from the linked list"""
    if head is None:
        print("Empty List")
        return head

    if head.data == n:  # If the first node contains the value
        print("Deleted item:", head.data)
        return head.next  # Update head to the next node

    prev = head
    temp = head.next

    while temp:
        if temp.data == n:
            prev.next = temp.next  # Remove the node by changing pointer
            print("Deleted item:", temp.data)
            return head  # Return the updated head
        prev = temp
        temp = temp.next

    print("Item Not Found")
    return head

# Main Menu
head = None
while True:
    print("\n**** Main Menu ****")
    print("1. INSERT AT END")
    print("2. DISPLAY")
    print("3. INSERT AT FIRST")
    print("4. COUNT")
    print("5. SEARCH")
    print("6. DELETE")
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
        print("No. of elements =", count(head))
    
    elif ch == 5:
        n = int(input("Enter data to search: "))
        pos = search(head, n)
        if pos > 0:
            print(f"Item found at position {pos}")
        else:
            print("Item not found")
    
    elif ch == 6:
        n = int(input("Enter data to delete: "))
        head = deletion(head, n)
    
    elif ch == 0:
        print("Exiting program...")
        break
    
    else:
        print("Wrong Input! Please try again.")