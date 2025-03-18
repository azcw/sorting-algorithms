import random
array = random.sample(range(10, 100), 20)
print(array)

def quicksort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quicksort(arr, left, position - 1)
        quicksort(arr, position + 1, right)
        
def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i <= j and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] 
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i 
    
quicksort(array, 0, len(array) - 1)
print(array)
