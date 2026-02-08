def moveZeroToEnd(nums):
    j=-1
    for i in range(0,len(nums)):
        if nums[i] == 0:
            j =i
            break
    print(j)
    for i in range(j+1, len(nums)):
        if nums[i] != 0:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = 0
            j = j + 1
    
    return nums


print(moveZeroToEnd([1,0,4,0,0,0,3,4,5,6]))
            