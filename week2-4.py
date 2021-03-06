def twoSum(nums, target):
    num1 = 0
    num2 = 0
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    


result=twoSum([2,11,7,15],9)
print(result)