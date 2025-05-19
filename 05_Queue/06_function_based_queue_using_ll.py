class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion(head, n, rear, front):
    if rear == None:
        head = Node(n)
        rear = head
        front = head
        return head, rear, front
    else:
        newnode = Node(n)
        rear.next = newnode
        rear = newnode
        return head, rear, front

def deletion(head, rear, front):
    if front == None:
        print("Empty Queue")
        return head, rear, front
    else:
        print("Deleted item", front.data)
        front = front.next
        head = front
        if front == None:
            rear = None
        return head, rear, front

def display(head):
    temp = head
    if temp == None:
        print("Empty Queue")
        return
    while temp:
        print(temp.data)
        temp = temp.next

# Main logic
head = None
rear = None
front = None

while True:
    print("\n**** Main Menu **** ")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Display")
    print("0. Exit")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        n = int(input("Enter data: "))
        head, rear, front = insertion(head, n, rear, front)
    elif ch == 2:
        head, rear, front = deletion(head, rear, front)
    elif ch == 3:
        display(head)
    elif ch == 0:
        break
    else:
        print("Wrong Input")
        pass