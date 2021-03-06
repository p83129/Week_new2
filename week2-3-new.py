def maxProduct(nums):
    max=0
    temp=0
        
    for i in range(len(nums)):
        for j in range(len(nums)):            
            if i!=j:
                temp=nums[i]*nums[j] 
                if max ==0:
                    max=temp                        
                if temp>max :
                    max=temp

    
    print(max)  
           
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])

