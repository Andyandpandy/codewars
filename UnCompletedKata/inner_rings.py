def spinning_rings(innerMax, outerMax):
    tempInnerMax = innerMax
    tempOuterMax = 1
    count = 1
    while tempInnerMax != tempOuterMax:
        
        if(tempInnerMax == 0):
            tempInnerMax = innerMax
        else:
             tempInnerMax -= 1
        if(tempOuterMax == outerMax):
            tempOuterMax = 0
        else:
            tempOuterMax += 1
        count += 1
    return count

print(spinning_rings(10, 2) == 10)
