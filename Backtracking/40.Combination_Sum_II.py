def find_coins(x):
    coins = [50, 20, 10, 5, 1]
    used = []
    for c in coins:
        if x >= c:
            x -= c                  # x = x - c
            used.append(c)   # 用過的硬幣放進c
        if x == 0:   # 提早結束
            break
    if x == 0:
        used.sort()
        return ",".join(map(str, used))      
    else:
        return "NOOOOO"
x = 26
print(find_coins(x))