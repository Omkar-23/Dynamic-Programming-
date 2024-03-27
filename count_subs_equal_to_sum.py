def count_subs(arr, target_sum , n ):
    t = [[0 if j > 0 else 1 for j in range(target_sum+1)] for i in range(n+1)]   
    for i in range(1,n+1):
            for j in range(1,target_sum+1):
                if j>=arr[i-1]:
                    t[i][j]=t[i-1][j] + t[i-1][j-arr[i-1]]
                else:
                    t[i][j] = t[i-1][j]
                

    
    return(t[n][target_sum])
    

if __name__ == '__main__':
    arr = [2,3,5,6,8,10]
    target_sum = 10 
    n = len(arr)
    print(count_subs(arr, target_sum ,n))