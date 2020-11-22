def find_it(seq):
    """
    Given an array, find the int that appears an odd number of times.

    There will always be only one integer that appears an odd number of times.
    :param seq: 
    :return: 
    """
    for x in seq:
        if seq.count(x) % 2 == 1:
            return x



print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)