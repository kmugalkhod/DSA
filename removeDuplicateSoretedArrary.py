def removeDuplicateSorredArray(nums):
    
    i = 0
    j = 1
    for j in range(1,len(nums)):
        
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i = i+ 1
    
    print(nums)
    return i


print(removeDuplicateSorredArray([1,1,2,2,2,3,3]))
