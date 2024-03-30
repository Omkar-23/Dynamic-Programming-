#submitted soln 
class Solution:
    
    def rod_cut(self, price, n):
        t = [0] * (n+1)
        
        for i in range(1, n+1):
            for j in range(1, n+1): 
                if i <= j:
                    t[j] = max(price[i-1] + t[j-i], t[j])
                    
        return t[n]

# def rod_cut(price, len_rod, n, le):
#     t = [[0 for i in range(n+1)] for i in range(le+1)]
#     for i in range(le+1):
#         for j in range(n+1):
#             if i ==0 or j ==0:
#                 t[i][j] =0
#             elif(len_rod[i-1]<=j):
#                 t[i][j] = max(price[i-1]+t[i][j-len_rod[i-1]],t[i-1][j])
#             else:
#                 t[i][j] = t[i-1][j]
#     return t[le][n]

if __name__ == '__main__':
    n = 8
    price =[3, 5, 8, 9, 10, 17, 17, 20]
    le = len(price)
    len_rod = [i for i in range(1,le+1)]
    print(rod_cut(price, len_rod, n, le))

