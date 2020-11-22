def friend(x):
    #Code
    current_list = []
    for name in x:
        if len(name) == 4 : current_list.append(name)
    return current_list

print(friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"])
