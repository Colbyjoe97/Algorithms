# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def moveZeroes(nums):
    count = nums.count(0)
    print(count)
    for i in range(count):
        nums.remove(0)
        nums.append(0)
    return nums

print(moveZeroes([0,0,1]))