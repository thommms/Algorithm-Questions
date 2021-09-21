'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]

Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1


Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
'''

def findMax(nums):
  currMax =0
  newMax =0
  count=0
  for val in nums:
    if val==1:
      currMax+=1
      newMax =max(currMax, newMax)
    else:
      currMax=0
  return (newMax)
