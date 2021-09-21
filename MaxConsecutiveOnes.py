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
  print (newMax)
