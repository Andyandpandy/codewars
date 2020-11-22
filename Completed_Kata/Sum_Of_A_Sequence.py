def sequence_sum(begin_number, end_number, step):
    x = 0
    for i in range(begin_number, end_number+1, step):
        x += i
    return x

def sequence_sum_oneliner(begin, end, step):
    return sum(range(begin,end+1,step))

print(sequence_sum(2, 6, 2), 12)
print(sequence_sum(1, 5, 1), 15)

print(sequence_sum_oneliner(2, 6, 2), 12)
print(sequence_sum_oneliner(1, 5, 1), 15)


