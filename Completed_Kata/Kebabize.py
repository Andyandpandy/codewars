

def kebabize(string):
    counter = 0
    result = ""
    if string[0].isupper():
        result += string[0].lower()
        counter += 1
    while counter < len(string):
        if string[counter].isdigit():
            counter += 1
        elif string[counter].isupper() and len(result) != 0:
            result += "-"
            result += string[counter].lower()
            counter += 1
        else:
            result += string[counter].lower()
            counter += 1
    return result

print(kebabize('myCamelCasedString'), 'my-camel-cased-string')
print(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
print(kebabize('SOS'), 's-o-s')
print(kebabize('42'), '')
print(kebabize('81Dd1eC9X'), 'dde-c-x')