def unionArray(nums1,nums2):
    
    # Take a length of nums1    
    n1 = len(nums1)

    # Take a length of nums2
    n2 = len(nums2)

    # Take Fist counter will itreate through nums1
    i = 0

    # Take Second counter will iterate through nums2
    j = 0

    # Initalise union array
    uniArray = []

    # Iterate both arrays n1 and n2
    while(i<n1 and j<n2):

        if (nums1[i] <= nums2[j]):
            if (len(uniArray)==0 or uniArray[len(uniArray) - 1] != nums1[i]):
                uniArray.append(nums1[i])
            i = i + 1
        else:
            if (len(uniArray)==0 or uniArray[len(uniArray) - 1] != nums2[j]):
                uniArray.append(nums2[j])
            j = j + 1

    while(i<n1):
        if (len(uniArray)==0 or uniArray[len(uniArray) - 1] != nums1[i]):
            uniArray.append(nums1[i])
        i = i + 1

    while(j<n2):
        if (len(uniArray)==0 or uniArray[len(uniArray) - 1] != nums2[j]):
            uniArray.append(nums2[j])
        j = j + 1
    
    return uniArray


print(unionArray([0,1,2,3,4,4,5,6,],[1,2,3,4,5,6]))
    


