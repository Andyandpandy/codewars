def sum_two_smallest_numbers(numbers):
    smallest = []
    for integer in numbers:
        if len(smallest) < 2:
            smallest.append(integer)
        elif smallest[0] > integer or smallest[1] > integer:
            smallest[smallest.index(max(smallest))] = integer
    return sum(smallest)

def sum_two_smallest_numbers_oneliner(numbers):
    return sum(sorted(numbers[:2]))

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
print(sum_two_smallest_numbers_oneliner([5, 8, 12, 18, 22]), 13)