'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

def sortedSquares(self, nums: List[int]) -> List[int]:
    res =[]
    for val in nums:
        res.append(val**2)
    res.sort()
    return (res)

nums= [-4,-1,0,3,10]
squaresOfSortedArray(nums)
  
'''
Alternate solution without using the sort function 
'''
# def squaresOfSortedArray(nums):
#     res =[]
#     l=0
#     r=len(nums)-1

#     for i in range(len(nums)-1, -1, -1):
#         if abs(nums[l])<abs(nums[r]):
#             res.insert(0,nums[r]**2)
#             r-=1
#         else:
#             res.insert(0,nums[l]**2)
#             l+=1
#     return (res)


