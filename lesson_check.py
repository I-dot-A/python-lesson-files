import random

def insertionSort(arr): # geeksforgeeks
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def IS_answer(L):
    """Sorts a list using insertion sort"""
    for i in range(1, len(L)):
        index = i
        j = i - 1
        while L[index] < L[j] and j >= 0:
            L[index], L[j] = L[j], L[index]
            index = j
            j = j - 1
    return L

# Homework:
def insertion_sort (nums):
    for i in range(1, len(nums)):
        while nums[i] < nums[i-1] and i > 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
    return nums

print(insertion_sort([0,5,1,2,4,10,24,11,45,34,78,98,52]))

for i in range(100):
    break_it = False
    L = random.sample(range(-1000,1000), 300)
    print(insertion_sort(L))
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            print("FAILURE SPOTTED")
            break_it = True
            break
    if break_it: break