def xo(s):
    """
      Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
    :param s: 
    :return: 
    """
    if not "x" in s or not "o" in s : return True
    x = 0
    o = 0
    for letter in list(s):
        if letter == "x": x += 1
        if letter == "o": o += 1
    return x == o
