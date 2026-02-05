
def leftRoate(nums):

    temp = nums[0]

    for i in range(1,len(nums)):
        nums[i-1] = nums[i]

    nums[len(nums) - 1] = temp

    return nums


print(leftRoate([1,2,3,4,5]))
