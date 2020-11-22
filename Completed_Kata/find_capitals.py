def capitals(word):
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list_result = []
    for index in range(0,len(word)):
        if word[index] in cap:
            list_result.append(index)
    return list_result

#forgot word.isUpper()


print(capitals('CodEWaRs'), [0,3,4,6])