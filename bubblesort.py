import random
array = random.sample(range(100), 20)
print(array)

def bubblesort(array):
    passes = len(array) - 1
    swaps = True
    while passes > 0 and swaps:
        swaps = False
        for i in range(passes):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps = True  
        passes -= 1
    return array

print(bubblesort(array))