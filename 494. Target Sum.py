def count_subs(arr, target_sum, n):
    t = [[0] * (target_sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        t[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if j >= arr[i - 1]:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][target_sum]

if __name__ == '__main__':
    arr = [1]
    diff = 2
    n = len(arr)
    if sum(arr) < diff or (sum(arr) + diff) % 2 != 0:
        print(0)
    else:
        target_sum = (diff + sum(arr)) // 2
        print(count_subs(arr, target_sum, n))
