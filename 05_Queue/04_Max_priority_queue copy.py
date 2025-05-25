class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item, priority):
        """Add an item with its priority to the queue"""
        self.items.append((priority, item))
        # Sort items each time to keep them in priority order
        self.items.sort(reverse=True)
    
    def pop(self):
        """Remove and return the item with highest priority (lowest number)"""
        if not self.is_empty():
            return self.items.pop(0)[1]  # Return just the item (not the priority)
        else:
            return "Queue is empty"
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return how many items are in the queue"""
        return len(self.items)
    
    def peek(self):
        """Look at the highest priority item without removing it"""
        if not self.is_empty():
            return self.items[0][1]  # Return just the item (not the priority)
        else:
            return "Queue is empty"

# Let's test our priority queue
pq = PriorityQueue()

# Add some tasks with different priorities
pq.push("Do homework", 3)    # Lower numbers = higher priority
pq.push("Eat lunch", 1)
pq.push("Watch TV", 4)
pq.push("Call mom", 2)

print("What's next?", pq.peek())  # Eat lunch (priority 1)

print("\nDoing tasks in order:")
while not pq.is_empty():
    task = pq.pop()
    print("Doing:", task)