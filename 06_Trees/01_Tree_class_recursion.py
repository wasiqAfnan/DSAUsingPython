# Complete class-based Binary Search Tree (BST) code that includes:

# Node and Tree classes

# insert(), search(), min(), max() functions

# Tree traversals: inorder, preorder, postorder

# A menu-driven interaction in main

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def search(self, node, key):
        if node is None:
            print("Data Not Found")
            return
        if node.data == key:
            print("Data Found")
        elif key < node.data:
            self.search(node.left, key)
        else:
            self.search(node.right, key)

    def find_min(self, node):
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def find_max(self, node):
        if node is None:
            return None
        current = node
        while current.right is not None:
            current = current.right
        return current.data

# ===== Menu-Driven Interaction =====
if __name__ == "__main__":
    tree = Tree()
    root = None

    while True:
        print("\n**** Main Menu ****")
        print("1. Insert")
        print("2. Inorder Traversal")
        print("3. Preorder Traversal")
        print("4. Postorder Traversal")
        print("5. Search")
        print("6. Find Minimum")
        print("7. Find Maximum")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to insert: "))
            root = tree.insert(root, value)

        elif choice == 2:
            if root:
                print("Inorder Traversal:")
                tree.inorder(root)
                print()
            else:
                print("Tree is empty.")

        elif choice == 3:
            if root:
                print("Preorder Traversal:")
                tree.preorder(root)
                print()
            else:
                print("Tree is empty.")

        elif choice == 4:
            if root:
                print("Postorder Traversal:")
                tree.postorder(root)
                print()
            else:
                print("Tree is empty.")

        elif choice == 5:
            if root:
                key = int(input("Enter value to search: "))
                tree.search(root, key)
            else:
                print("Tree is empty.")

        elif choice == 6:
            if root:
                print("Minimum value:", tree.find_min(root))
            else:
                print("Tree is empty.")

        elif choice == 7:
            if root:
                print("Maximum value:", tree.find_max(root))
            else:
                print("Tree is empty.")

        elif choice == 0:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
