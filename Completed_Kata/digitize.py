def digitize(n):
    """
    Convert number to reversed array of digits
    Given a random number:
    
    You have to return the digits of this number within an array in reverse order.
    :param n: integer
    :return: reversed order of digits in list
    """
    my_list = []
    for x in list(str(n)) : my_list.append(int(x))
    my_list.reverse()
    return my_list

print(digitize(35231),[1,3,2,5,3])
