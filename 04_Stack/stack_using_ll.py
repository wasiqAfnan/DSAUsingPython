# Node class to store data and next pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed to stack.")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack is empty. Cannot pop.")
        else:
            popped = self.top.data
            self.top = self.top.next
            print(f"{popped} popped from stack.")

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print(f"Top element is {self.top.data}")

    # Display the stack
    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            current = self.top
            print("Stack elements:")
            while current:
                print(current.data)
                current = current.next

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.peek()
stack.pop()
stack.display()