def reverse_words(s):
    """
    Write a reverseWords function that accepts a string a parameter, 
    and reverses each word in the string. Any spaces in the string should be retained.

    Example:
    
    reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
    reverse_words("double  spaces") # returns  "elbuod  secaps"
    :param s: a string
    :return: s reversed
    """

    split_s = s.split()
    new_string = ""
    counter = 0
    for i in range(0,len(split_s)):
        while s[counter] == " ":
            new_string += " "
            counter += 1
        current_string = list(split_s[i])
        current_string.reverse()
        for char in current_string:
            new_string += char
        counter += len(current_string)

    return new_string

print(reverse_words("double  spaces"))