# Kadane’s Algorithm
# return max value
def find_maximum_subarray(x):
    max_sum = x[0]
    current_sum = 0
    for i in range(len(x)):
        current_sum += x[i]
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

x = [1, 2, -2, -3, 5]
print(find_maximum_subarray(x))
