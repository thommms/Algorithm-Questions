import numpy as np

def deadlockPrevention(need,currAvailable,allocation):
  output =[]
  processes = ""
  tracker = 0
  deadlock_checker=0
  while (tracker<len(currAvailable)):
    for n in need:
      need_index = need.index(n)
      if checkIfNeed(n,currAvailable,need_index)!=-1:
        # processes.append(need_index)
        all_index = checkIfNeed(n,currAvailable,need_index)

        if allocation[all_index] not in output:
          output.append(allocation[all_index])
          processes+="P"
          processes+=str(need_index);
          processes+=", "

          print ("\n>> For process P%d"%need_index)
          print ("Total allocation: ",allocation)
          print ("process to be completed in the allocation: ",allocation[need_index])
          print ("currently available: ",currAvailable)
          currAvailable = list(map(lambda x,y: x+y, currAvailable,allocation[all_index]))
          # need.remove(need[i+1])
          print ("\nAfter process execution...\n")
          print ("new currently available resources: ",currAvailable)
          print ("==================")
    tracker+=1
    deadlock_checker+=1
    if deadlock_checker>len(currAvailable):
      return "DEADLOCK OCCURS... HENCE TERMINATED"
  print ("\nTo prevent deadlock, run the processes in this order: ",processes)
  print ("Here are the resources of the process",output)
  print ("upon process completion, the available resources are ",currAvailable)



def totalAllocationUsed(allocation,number_processes):
  answer = []
  for column in range(number_processes-1):
    t=0
    for row in allocation:
      t+=row[column]
    answer.append(t)
  return answer

def checkIfNeed(needArr,currAvailable,need_index):
  count=0
  for i in range(len(needArr)):
    if currAvailable[i]>=needArr[i]:
      count+=1
    if count==len(currAvailable):
      return need_index
  return -1

def deadlockMain(totalResource,number_processes,allocation,amountNeeded):

  #The code below computes the need, current available resources and total allocation
  need= np.subtract(amountNeeded,allocation).tolist()
  totalAllocation = totalAllocationUsed(allocation,number_processes)
  currAvailable = np.subtract(totalResource,totalAllocation)

  print ("Need: ",need)
  print ("currently available: ",currAvailable)

  deadlockPrevention(need,currAvailable,allocation)

#=====================Running the code=================================================

#enter your inputs in these given arrays
totalResource=[6,8,7]
number_processes= 4
allocation=[[2,2,0],[3,2,0],[1,1,3],[0,0,2]]
amountNeeded =[[4,5,3],[3,2,3],[1,2,3],[1,0,2]]

deadlockMain(totalResource,number_processes,allocation,amountNeeded)