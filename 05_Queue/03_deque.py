from array import *

# Define the maximum size of the deque
MAX = 5

class DequeArray:
    """Class to implement a double-ended queue (deque) using an array"""
    def __init__(self):
        self.deque = array('i', [0] * MAX)  # Initialize deque with a fixed size
        self.rear = -1  # Rear pointer (points to last element)
        self.front = -1  # Front pointer (points to first element)

    def insertion_rear_end(self, n):
        """Function to insert an element at the rear end of the deque"""
        if self.rear == MAX - 1:
            print("Insertion Not Possible (Queue Overflow)")
        else:
            self.rear += 1
            self.deque[self.rear] = n  # Insert element at the rear
            print("One item added at rear")

    def insertion_front_end(self, n):
        """Function to insert an element at the front end of the deque"""
        if self.front == -1:
            print("Insertion Not Possible (Queue Underflow)")
        else:
            self.deque[self.front] = n  # Insert element at the front
            self.front -= 1
            print("One item added at front")

    def deletion_front_end(self):
        """Function to delete an element from the front end of the deque"""
        if self.rear == self.front:
            print("Empty Deque (Underflow)")
        else:
            self.front += 1
            n = self.deque[self.front]  # Remove front element
            print("Deleted item =", n)

    def deletion_rear_end(self):
        """Function to delete an element from the rear end of the deque"""
        if self.rear == self.front:
            print("Empty Deque (Underflow)")
        else:
            n = self.deque[self.rear]  # Remove rear element
            self.rear -= 1
            print("Deleted item =", n)

    def display(self):
        """Function to display elements in the deque"""
        if self.rear == self.front:
            print("Empty Deque")
        else:
            print("The deque is given below:")
            i = self.front + 1
            while i <= self.rear:
                print(self.deque[i])  # Print deque elements
                i += 1

# Create deque object
dq = DequeArray()

# Main Menu for deque operations
while True:
    print("\n**** Main Menu ****")
    print("1. INSERTION REAR END")
    print("2. INSERTION FRONT END")
    print("3. DELETION FRONT END")
    print("4. DELETION REAR END")
    print("5. DISPLAY")
    print("0. EXIT")

    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        n = int(input("Enter data: "))
        dq.insertion_rear_end(n)

    elif ch == 2:
        n = int(input("Enter data: "))
        dq.insertion_front_end(n)

    elif ch == 3:
        dq.deletion_front_end()

    elif ch == 4:
        dq.deletion_rear_end()

    elif ch == 5:
        dq.display()

    elif ch == 0:
        print("Exiting program...")
        break

    else:
        print("Wrong Input! Please try again.")
