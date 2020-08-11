# TO-DO: complete the helper function below to merge 2 sorted arrays
from heapq import merge

def helper_merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [] * elements

    # Your code here
    a = b = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
    merged_arr += arrA[a:]
    merged_arr += arrB[b:]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])

    return helper_merge(low, high)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    s2 = mid + 1
    if arr[mid] <= arr[s2]:
        return
    while start <= mid and s2 <= end:



def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        mid = l + (r - 1) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)


