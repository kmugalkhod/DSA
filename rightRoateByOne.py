

# [1,2,3,4,5,6]

# Roatate By 1 

# [6,1,2,3,4,5]

# [5,6,1,2,3,4]

def rightRotateByOne(nums):
    temp = nums[len(nums) -1]

    for i in range(len(nums)-1,0,-1):
        nums[i] = nums[i-1]

    nums[0] = temp

    return nums

# print(rightRotateByOne([1,2,3,4,5]))



def rightRotateByD(nums,d):
    temp = nums[-d:]

    for i in range(len(nums)-d,0,-1):
        new_index = i-d
        if (i-d) >=0:
            nums[i] = nums[new_index]

    
    for i in range(0,len(temp)):
        nums[i] = temp[i]
    
    return nums
        

print([1,2,3,4,5,6])
print(rightRotateByD([1,2,3,4,5,6],1))
           
