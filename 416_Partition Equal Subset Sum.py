def partition(nums,sum,n,mn_sum):
    if(mn_sum %2!=0):
        return False
    else:
        t = ([[False for  i in range(sum+1)] for i in range(n+1)])
        for i in range(n+1):
            t[i][0]=True
        for i in range(1,sum+1):
            t[0][i]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j < nums[i-1]:
                t[i][j]=t[i-1][j]
            if(j>=nums[i-1]):
                t[i][j]=t[i-1][j]or t[i-1][j-nums[i-1]]
    
    
    return t[n][sum]
        
       
if __name__ == '__main__':
    nums = [1,5,11,5]
    n = len(nums)
    total_sum = sum(nums)
    target_sum = total_sum // 2
    res = partition(nums, target_sum, n, total_sum)
    print(res)
    