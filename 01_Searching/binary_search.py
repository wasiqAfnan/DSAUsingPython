def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Define the search range

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half

    return -1  # Return -1 if target is not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")