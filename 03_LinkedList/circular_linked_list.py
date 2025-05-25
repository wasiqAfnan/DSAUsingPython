class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_position(head, data, position):
    new_node = Node(data)

    if position == 1:
        if head is None:
            new_node.next = new_node
            head = new_node
        else:
            temp = head
            while temp.next != head:
                temp = temp.next
            new_node.next = head
            temp.next = new_node
            head = new_node
        return head

    temp = head
    count = 1
    while count < position - 1 and temp.next != head:
        temp = temp.next
        count += 1

    if temp.next == head and count < position - 1:
        print("Position out of bounds")
        return head

    new_node.next = temp.next
    temp.next = new_node
    return head


def delete_by_value(head, value):
    if head is None:
        print("Empty List")
        return head

    current = head
    prev = None

    # Deleting head node
    if current.data == value:
        if head.next == head:  # Only one node
            print("Deleted:", head.data)
            return None
        else:
            while current.next != head:
                current = current.next
            current.next = head.next
            print("Deleted:", head.data)
            head = head.next
            return head

    prev = head
    current = head.next

    while current != head:
        if current.data == value:
            prev.next = current.next
            print("Deleted:", value)
            return head
        prev = current
        current = current.next

    print("Item not found")
    return head


def display(head):
    if head is None:
        print("Empty List")
        return
    print("Circular Linked List contents:")
    temp = head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == head:
            break
    print("(head)")


# 🔹 Menu-driven driver code
def main():
    head = None
    while True:
        print("\nCircular Linked List Menu:")
        print("1. Insert at position")
        print("2. Delete by value")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter data to insert: "))
            pos = int(input("Enter position to insert at: "))
            head = insert_at_position(head, data, pos)

        elif choice == '2':
            val = int(input("Enter value to delete: "))
            head = delete_by_value(head, val)

        elif choice == '3':
            display(head)

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

main()
