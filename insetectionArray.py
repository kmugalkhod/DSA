def intersectionOfArray(nums1,nums2):
    # Calculate length of nums1 array
    print("Kunal")
    n1 = len(nums1)
    # Calculate length of nums2 array
    n2 = len(nums2)

    #Comparing both n1 to decide for which indexMapArray should be created

    indexMapArrayLength = 0

    if (n1 > n2):
        indexMapArrayLength = n2
    else:
        indexMapArrayLength = n1
    
    #Create Dict to Map index 

    indexMapArray= {}
    for i in range (0,indexMapArrayLength):
        print(i)
        indexMapArray[i] = 0

    print(indexMapArray)    
    # interate both array to calculate the intersection 


    i =0 
    j =0
    unionArray = []
    for i in range(0,n1):
        for j in range(0,n2):
            if nums2[j] > nums1[i]:
                break
            else:
                if  nums2[j] == nums1[i] and indexMapArray[j] == 0:
                    unionArray.append(nums2[j])
                    indexMapArray[j] = 1
    
    return unionArray


def intersectionOfArrayOptimum(nums1,nums2):

    # Calculate the length of for each array
    n1 = len(nums1)
    n2 = len(nums2)

    #Initalise Counter
    i= 0 
    j= 0

    #initalize union Array
    unionArray = []

    while(i<n1 and j <n2):
        if nums1[i] < nums2[j]:
            i = i +1 
        if nums2[j] < nums1[i]:
            j = j +1
        
        if nums1[i] == nums2[j]:
            unionArray.append(nums1[i])
            i = i + 1
            j = j + 1
    
    return unionArray 
            


print(intersectionOfArray([1,2,3,4,5,6], [2,3,4]))


print(intersectionOfArrayOptimum([1,2,3,4,5,6], [2,3,4]))

# 1 2 3 4 5 6

# 2 3 4
