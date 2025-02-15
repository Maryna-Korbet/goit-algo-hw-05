def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None  

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]  
        
        if arr[mid] < target:
            left = mid + 1
        else:
            # Update upper_bound
            upper_bound = arr[mid]  
            right = mid - 1

    # If target is not found, we return upper_bound
    return iterations, upper_bound  

# A basic sorted array of fractional numbers
main_array = [0.5, 1.3, 2.7, 3.9, 4.2, 5.6, 6.8, 7.1, 8.5, 9.9]

# Теst 1: target = 3.0
target = 3.0
result = binary_search(main_array, target)
print("\n--- Test 1: target = 3.0 ---")
print(f"Number of iterations: {result[0]}")
print(f"Upper bound: {result[1]}")  # Output: (2, 3.9)

# Теst 2: target = 10.0
target = 10.0
result = binary_search(main_array, target)
print("\n--- Test 2: target = 10.0 ---")
print(f"Number of iterations: {result[0]}")
print(f"Upper bound: {result[1]}")  # Output: (4, None)

# Теst 3: target = 0.0
target = 0.0
result = binary_search(main_array, target)
print("\n--- Test 3: target = 0.0 ---")
print(f"Number of iterations: {result[0]}")
print(f"Upper bound: {result[1]}")  # Output: (1, 0.5)


