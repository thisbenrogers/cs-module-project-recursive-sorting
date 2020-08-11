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
    pass


def merge_sort_in_place(arr, l, r):
    # ? To explain what is going on here:
    # ?     This algorithm is merging increasingly
    # ?     larger portions (doubling) of the input arr.
    # ?     
    # ?     72 doubles the tracker until it's large enough to escape
    # ?     the 'while' on 58, then the sorted array is returned
    # ?     
    # ?     60 ues the doubling-tracker for steps in the range, 
    # ?     61 uses min() to smoothly transition values on later passes
    # ?
    # ?     Much of the work is happening in the slicing
    # ?     assigments on line 69, then the swap on 71

    tracker = 1
    while tracker <= len(arr):
        h = 0
        for h in range(0, len(arr), tracker * 2):
            left, right = h, min(len(arr), h + 2 * tracker)
            mid = h + tracker
            p, q = left, mid
            while p < mid and q < right:
                if arr[p] <= arr[q]:
                    p += 1
                else:
                    temp = arr[q]
                    arr[p + 1: q + 1] = arr[p:q]
                    arr[p] = temp
                    p, mid, q = p + 1, mid + 1, q + 1
        tracker *= 2
    return arr


