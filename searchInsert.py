# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# SLIGHTLY SLOWER SOLUTION
def searchInsert(nums, target):
        for i in range(len(nums)):
            if target in nums:
                if nums[i] == target:
                    return i
            else:
                newArr = []
                for i in range(len(nums)):
                    if nums[i] + 1 > target:
                        newArr.append(target)
                        return i
                    elif i == len(nums) - 1:
                        newArr.append(target)
                        return i + 1
                    else:
                        newArr.append(nums[i])


print(searchInsert([1,3,5,6], 2))

# FASTER SOLUTION
# def searchInsert(self, nums, target):
#         low = 0
#         high = len(nums) - 1
#         mid = 0

#         while low <= high:

#             mid = (high + low) // 2 

#             if nums[mid] < target:
#                 low = mid + 1

#             elif nums[mid] > target:
#                 high = mid - 1

#             else:
#                 return mid

#         return low