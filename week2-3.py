def maxProduct(nums):
    
    # 方法一:直接用sort()反向排序
    # print(nums[0])
    # y = sorted(nums, reverse = True)
    # print(y) 

    # 方法二:直接用氣泡排序
    N = len(nums)
    for i in range(N-1):        
        for j in range(N-i-1):            
            if nums[j]>nums[j+1]:                
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp 

    # print(nums)
    num1 = nums[N-1]
    num2 = nums[N-2]
    print(num1*num2)            
           
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
