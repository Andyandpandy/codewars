def evaporator(content, evap_per_day, threshold):
    """
    This program tests the life of an evaporator containing a gas.
   
    All parameters are strictly positive numbers.

    The program reports the nth day (as an integer) on which the evaporator will be out of use.

    Note : Content is in fact not necessary in the body of the function "evaporator", 
    you can use it or not use it, as you wish. 
    Some people might prefer to reason with content, 
    some other with percentages only. 
    It's up to you but you must keep it as a parameter because the tests have it as an argument.
    
    :param content: We know the content of the evaporator (content in ml)
    :param evap_per_day: the percentage of foam or gas lost every day (evap_per_day)
    :param threshold: the threshold (threshold) in percentage beyond which the evaporator is no longer useful.
    :return: 
    """
    totalcontent = content
    counter = 0
    while totalcontent / 100 * threshold < content:
        content -= content / 100 * evap_per_day
        counter += 1
    return counter

print((evaporator(10, 10, 10), 22))