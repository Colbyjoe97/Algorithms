# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


# WITHOUT USING NUMS.SORT()
def sortedSquares(nums):
        for n in range(len(nums)):
            nums[n] = nums[n] * nums[n]
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


# USING NUMS.SORT()
# def sortedSquares(nums):
#         for n in range(len(nums)):
#             nums[n] = nums[n] * nums[n]
#         nums.sort()
#         return nums


print(sortedSquares([-4,-1,0,3,10]))