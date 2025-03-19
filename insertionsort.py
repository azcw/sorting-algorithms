import random
nums = random.sample(range(200), 20)
print("Before Sort: ", nums)

def insert(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
    
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums [j]
            j = j - 1
        nums[j+1] = key
        
insert(nums)
print("After Sort: ", nums)

