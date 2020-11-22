def to_binary(n):
    b = ''
    print(bin(n))

    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    elif n > 1:
        value = 1
        while 2**value < n:
            if 2**(value+1) <= n:
                value += 1
            else:
                break
        if value == 1:
            return "10"
        else:
            while n > 1:
                if 2 ** value < n:
                    b += "1"
                    n = n // 2
                elif 2 ** value == n:
                    b += "1"
                    n = n // 2
                    while n > 0:
                        b += "0"
                        n = n // 2
                else:
                    b += "0"
                    value -= 1
            if n == 1:
                b += "1"
    else:
        print("negative")

    return b

print(to_binary(2),"10")
print(to_binary(3),"11")
print(to_binary(4),"100")
print(to_binary(8),"1000")
print(to_binary(16),"10000")
print(to_binary(5),"101")
print(to_binary(17),"10001")
print(to_binary(-3),"11111111111111111111111111111101")
print(to_binary(0),"0")