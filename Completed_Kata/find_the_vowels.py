def vowel_indices(word):
    word = word.lower()
    vowels = ("a","e","i", "o", "y", "u")
    result = []
    for index in range(0,len(word)):
        if word[index] in vowels:
            result.append(index+1)
    return result

