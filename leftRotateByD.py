


def reversedbyD(nums,start,end):

    while(start<=end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start = start + 1
        end =  end - 1
    
    return nums
  




def leftRoatebyD(nums,d):
    actualD = d%len(nums)

    temp = nums[:actualD]

    for i in range(actualD,len(nums)):
        nums[i-actualD] = nums[i]

    
    for i in range(0,len(temp)):
        index = len(nums) - actualD + i
        nums[index] = temp[i]

    return nums


def leftRoatebyDOptimum(nums,d):
    d = d%len(nums)
    nums = reversedbyD(nums,0,d-1)
    nums = reversedbyD(nums,d,len(nums)-1)
    nums = reversedbyD(nums,0,len(nums)-1)
    print(nums)
    
# print(reversedbyD([1,2,3,4,5,6],0,2))


print(leftRoatebyDOptimum([1,2,3,4,5,6],3))


