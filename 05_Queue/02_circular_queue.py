from array import *

# Define the maximum size of the circular queue
MAX = 5

class CircularQueue:
    """Class to implement a circular queue using an array"""
    def __init__(self):
        self.cqueue = array('i', [0] * MAX)  # Initialize queue with fixed size
        self.rear = 0  # Points to the position where the next element will be inserted
        self.front = 0  # Points to the first element of the queue

    def insertion(self, n):
        """Function to insert an element into the circular queue"""
        if (self.rear + 1) % MAX == self.front:
            print("QUEUE OVERFLOW")  # Queue is full
        else:
            self.cqueue[self.rear] = n  # Insert element at rear
            self.rear = (self.rear + 1) % MAX  # Move rear in circular manner
            print("One item added")

    def deletion(self):
        """Function to delete an element from the circular queue"""
        if self.rear == self.front:
            print("Empty Queue")  # Queue is empty
        else:
            n = self.cqueue[self.front]  # Get the front element
            self.front = (self.front + 1) % MAX  # Move front in circular manner
            print("Deleted item =", n)

    def display(self):
        """Function to display elements in the circular queue"""
        if self.rear == self.front:
            print("Empty Queue")  # Queue is empty
        else:
            print("The Queue is given below:")
            i = self.front
            while i != self.rear:
                print(self.cqueue[i])  # Print queue elements
                i = (i + 1) % MAX  # Move index in circular manner

# Create circular queue object
cq = CircularQueue()

# Main Menu for circular queue operations
while True:
    print("\n**** Main Menu ****")
    print("1. INSERTION")
    print("2. DELETION")
    print("3. DISPLAY")
    print("0. EXIT")
    
    ch = int(input("Enter Your Choice: "))
    
    if ch == 1:
        n = int(input("Enter data: "))
        cq.insertion(n)
    
    elif ch == 2:
        cq.deletion()
    
    elif ch == 3:
        cq.display()
    
    elif ch == 0:
        print("Exiting program...")
        break
    
    else:
        print("Wrong Input! Please try again.")
