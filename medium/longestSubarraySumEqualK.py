
def longestSubArraySumEqualk(nums,k):
    sum = 0 
    preMap = {}
    maxLen = 0

    for i in range(0,len(nums)):
        sum = sum + nums[i]

        if(sum == k):
            maxLen = max(maxLen, i +1)
        
        rem = sum - k 

        if rem in preMap:
            len1 =  i - preMap[rem] 
            print(rem)
            maxLen = max(maxLen,len1)
        
        if sum not in preMap:
            preMap[sum] = i


    print(preMap)   
    return maxLen


print(longestSubArraySumEqualk([1,2,3,1,1,1,4,5,6],3))

