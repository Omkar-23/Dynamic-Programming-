def knapSack(wt, val, W, N):
    t = [[0 for i in range(W+1)] for i in range(N+1)]
    for i in range(N+1):
        for j in range(W+1):
            if i ==0 or j ==0 :
                t[i][j] ==0 
            elif(wt[i-1]<=j):
                t[i][j] = max(val[i-1]+t[i][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    
    return t[N][W]



if __name__ == '__main__':
    N= 2
    W= 3
    val = [1,1]
    wt = [2,1]
    print(knapSack(wt,val,W,N))
