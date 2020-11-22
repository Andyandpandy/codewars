
def comp(array1, array2):
    # your code
    array1 = set(array1)
    array2 = set(array2)
    for number in array1:
        if not number**2 in array2:
            return False
        else:
            while number ** 2 in array2:
                array2.remove(number**2)
    if len(array2) > 0:
        return False
    return True

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 132, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a,b))
