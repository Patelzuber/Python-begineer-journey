nums = (78,98,65,56,23,987,567,12,57,92,10)
x = 23
i = 0
while i < len(nums):
  if(nums[i] == x):
    print("found at idx : ",i)
    break
  else:
    print("finding....")
    i += 1
    print("end of the loop")
    
