# Kadane’s Algorithm
# 回傳最大連續子序列

def find_max_subarray(x):
    max_sum = x[0]
    cur_sum = 0
    best_left = 0  #右邊界
    best_right = 0 #左邊界
    left_index = 0 #候選左邊界

    for i in range(len(x)):
        cur_sum += x[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            best_right = i
            if best_right > left_index: # 右邊界要大於候選左邊界才代表是同一對的
                best_left = left_index  # 把候選左邊界定義為正式的
        elif cur_sum < 0:
            cur_sum = 0
            left_index = i + 1 
    return x[best_left:best_right + 1]

x = [1, 2, -2, -3, 5, 3]
print(find_max_subarray(x))