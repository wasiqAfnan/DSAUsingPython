# Node class to store data and next pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class using linked list
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} enqueued to queue.")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue is empty. Cannot dequeue.")
        else:
            removed = self.front.data
            self.front = self.front.next
            if self.front is None:  # Queue became empty
                self.rear = None
            print(f"{removed} dequeued from queue.")

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print(f"Front element is {self.front.data}")

    # Display the queue
    def display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            current = self.front
            print("Queue elements:")
            while current:
                print(current.data)
                current = current.next

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.peek()
queue.dequeue()
queue.display()
