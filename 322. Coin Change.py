def change(coins, amount,n):
    t=[[0 for x in range(amount+1)]  for x in range(n+1) ]
    for i in range(1, n + 1):
        t[i][0] = 0
    for j in range(1, amount + 1):
        t[0][j] = float('inf') - 1

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                t[i][j] = min(1 + t[i][j - coins[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    ans = -1 if t[n][amount] == float('inf') - 1 else t[n][amount]
    return ans

if __name__ =='__main__':
    coins = [1,2,5]
    amount = 11
    n =  len(coins)
    print(change(coins , amount , n))