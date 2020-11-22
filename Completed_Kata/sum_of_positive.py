def positive_sum(arr):
    # Your code here
    result = 0
    for number in arr:
        if number > 0:
            result += number
    return result
