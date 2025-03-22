from array import *

# Define the maximum size of the stack
MAX = 5

class StackArray:
    """Class to implement a stack using an array"""
    def __init__(self):
        self.stack = array('i', [0] * MAX)  # Initialize stack with fixed size
        self.top = -1  # Stack is initially empty

    def push(self, n):
        """Function to push an element onto the stack"""
        if self.top == MAX - 1:
            print("STACK OVERFLOW")  # Stack is full, cannot push
        else:
            self.top += 1  # Increment top index
            self.stack[self.top] = n  # Insert element
            print("One item added")

    def pop(self):
        """Function to pop an element from the stack"""
        if self.top == -1:
            print("EMPTY STACK")  # Stack is empty, cannot pop
        else:
            n = self.stack[self.top]  # Get the top element
            self.top -= 1  # Decrement top index
            print("Deleted item =", n)

    def display(self):
        """Function to display elements in the stack"""
        if self.top == -1:
            print("EMPTY STACK")  # No elements to display
        else:
            print("The Stack is given below:")
            i = self.top
            while i >= 0:
                print(self.stack[i])  # Print stack elements from top to bottom
                i -= 1

# Create stack object
s = StackArray()

# Main Menu for stack operations
while True:
    print("\n**** Main Menu ****")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("0. EXIT")
    
    ch = int(input("Enter Your Choice: "))
    
    if ch == 1:
        n = int(input("Enter data: "))
        s.push(n)
    
    elif ch == 2:
        s.pop()
    
    elif ch == 3:
        s.display()
    
    elif ch == 0:
        print("Exiting program...")
        break
    
    else:
        print("Wrong Input! Please try again.")
