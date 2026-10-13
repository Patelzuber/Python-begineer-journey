nums = (1,4,6,78,35,234,76,89,14,15,76,123,65,76,143)

x = 89

i = 0
while i < len(nums):
  if(nums[i] == x):
    print("Found at idx : ",i)
    i += 1
