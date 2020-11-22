def remove_smallest(numbers):
    """
    
    :param numbers: list of numbers
    :return: new list without the lowest value in the numbers list
    """
    if len(numbers) > 0 : numbers.remove(min(numbers))
    return numbers

print(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])