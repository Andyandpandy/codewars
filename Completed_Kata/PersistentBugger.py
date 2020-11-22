def persistence(n):
    """
    Multiplicative persistence, 
    :param n: positive int
    :return: number of times you must multiply the digits in num untill you reach a single digit
    """
    count = 0
    list_of_n = list(str(n))
    while n > 9:
        result = 1
        for integer in list_of_n:
            result *= int(integer)
        n = result
        list_of_n = list(str(n))
        count += 1
    return count

print(persistence(39), 3)
print(persistence(999), 4)
print(persistence(4), 0)