from array import *

# Define the maximum size of the queue
MAX = 5

class QueueArray:
    """Class to implement a queue using an array"""
    def __init__(self):
        self.queue = array('i', [0] * MAX)  # Initialize queue with fixed size
        self.rear = -1  # Rear pointer (end of the queue)
        self.front = -1  # Front pointer (start of the queue)

    def insertion(self, n):
        """Function to insert an element into the queue"""
        if self.rear == MAX - 1:
            print("QUEUE OVERFLOW")  # Queue is full, cannot insert
        else:
            self.rear += 1  # Move rear pointer forward
            self.queue[self.rear] = n  # Insert element at rear
            print("One item added")

    def deletion(self):
        """Function to delete an element from the queue"""
        if self.rear == self.front:
            print("Empty Queue")  # Queue is empty, nothing to delete
        else:
            self.front += 1  # Move front pointer forward
            n = self.queue[self.front]  # Get the front element
            print("Deleted item =", n)

    def display(self):
        """Function to display elements in the queue"""
        if self.rear == self.front:
            print("Empty Queue")  # Queue is empty, nothing to display
        else:
            print("The Queue is given below:")
            i = self.front + 1  # Start from the first inserted element
            while i <= self.rear:
                print(self.queue[i])  # Print queue elements
                i += 1

# Create queue object
q = QueueArray()

# Main Menu for queue operations
while True:
    print("\n**** Main Menu ****")
    print("1. INSERTION")
    print("2. DELETION")
    print("3. DISPLAY")
    print("0. EXIT")
    
    ch = int(input("Enter Your Choice: "))
    
    if ch == 1:
        n = int(input("Enter data: "))
        q.insertion(n)
    
    elif ch == 2:
        q.deletion()
    
    elif ch == 3:
        q.display()
    
    elif ch == 0:
        print("Exiting program...")
        break
    
    else:
        print("Wrong Input! Please try again.")
