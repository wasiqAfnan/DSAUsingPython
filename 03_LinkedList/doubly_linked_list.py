class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insert_at_position(head, data, position):
    new_node = Node(data)

    if position == 1:
        new_node.next = head
        if head:
            head.prev = new_node
        head = new_node
        return head

    temp = head
    count = 1

    while temp and count < position - 1:
        temp = temp.next
        count += 1

    if temp is None:
        print("Position out of bounds")
        return head

    new_node.next = temp.next
    new_node.prev = temp

    if temp.next:
        temp.next.prev = new_node

    temp.next = new_node
    return head


def delete_by_value(head, value):
    if head is None:
        print("Empty List")
        return head

    temp = head

    if temp.data == value:
        head = temp.next
        if head:
            head.prev = None
        print("Deleted:", value)
        return head

    while temp and temp.data != value:
        temp = temp.next

    if temp is None:
        print("Item not found")
        return head

    if temp.prev:
        temp.prev.next = temp.next
    if temp.next:
        temp.next.prev = temp.prev

    print("Deleted:", value)
    return head


def display_forward(head):
    if head is None:
        print("Empty List")
        return
    print("List in forward direction:")
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")


def display_backward(head):
    if head is None:
        print("Empty List")
        return
    temp = head
    while temp.next:
        temp = temp.next
    print("List in backward direction:")
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.prev
    print("None")


# Menu-driven driver code
def main():
    head = None
    while True:
        print("\nDoubly Linked List Menu:")
        print("1. Insert at position")
        print("2. Delete by value")
        print("3. Display forward")
        print("4. Display backward")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter data to insert: "))
            pos = int(input("Enter position to insert at: "))
            head = insert_at_position(head, data, pos)

        elif choice == '2':
            val = int(input("Enter value to delete: "))
            head = delete_by_value(head, val)

        elif choice == '3':
            display_forward(head)

        elif choice == '4':
            display_backward(head)

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
