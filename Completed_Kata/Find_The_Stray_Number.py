def stray(arr):
    """
    You are given an odd-length array of integers, in which all of them are the same, except for one single number.

    Implement the method stray which accepts such array, and returns that single different number.
    
    The input array will always be valid! (odd-length >= 3)
    
    Examples:
    
    [1, 1, 2] => 2
    
    [17, 17, 3, 17, 17, 17, 17] => 3
    """
    if arr.count(arr[0]) == 1:
        return arr[0]
    else:
        common_value = arr[0]

    for i in range(0,len(arr)):
        if common_value != arr[i]:
            return arr[i]
    return 0

print(stray([1,1,1,1,1,1,2]) == 2)
print(stray([2,3,2,2,2]) == 3)
print(stray([3,2,2,2,2]) == 3)
