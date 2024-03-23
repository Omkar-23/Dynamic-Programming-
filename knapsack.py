def knapsack(weight,profit,cap, n):
    t=[[0 for x in range(cap+1)]  for x in range(n+1) ]
    for i in range(n+1):
        for j in range(cap+1):
            if cap == 0 or i == 0:
                t[i][j]= 0 
            elif(weight[i-1]<=cap):
                t[i][j]= max(profit[i-1]+t[i-1] [cap-weight[i-1]],t[i-1][j])
            else:
                t[i][j]= t[i-1][j]

    return t[n][cap]           




if __name__ =='__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    cap = 60
    n = len(profit)
    print(knapsack(weight,profit,cap,n))