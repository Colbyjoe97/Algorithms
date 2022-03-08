# Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    for i in range(k):
        nums.insert(0, nums.pop())
    print(nums)


rotate([1,2,3,4,5], 3)
