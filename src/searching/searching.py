# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if not arr: # return -1 if list is empty
        return -1

    while end >= start:
        mid = (start + end) // 2
        if arr[mid] == target: # if the mid is the target
            return mid
        if arr[mid] < target: # if the target is larger than the mid
            return binary_search(arr, target, mid + 1, end) 
        return binary_search(arr, target, start, mid - 1) # if the target is smaller than the mid
    return -1 # not found
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    if not arr:
        return -1

    start = 0
    end = len(arr) - 1

    is_ascending = arr[start] < arr[end]

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if is_ascending:
            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < target:
                end = mid - 1
            else:
                start = mid + 1
    return -1

