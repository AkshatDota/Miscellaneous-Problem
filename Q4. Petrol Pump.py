# 1 2 3 4 5 10 11 3 6 16

l = list(map(int, input().split()))
n = len(l)
sums = sum(l)
dp = [[0 for j in range(sums+1)] for i in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(1, sums+1): # Not required since I have already initialized above
    dp[0][i] = 0
for i in range(1, n+1):
    for j in range(1, sums+1):
        dp[i][j] = dp[i-1][j]
        
        if(l[i - 1] <= j):
            idx = j - l[i-1]
            dp[i][j] |= dp[i-1][idx]

            
            
for i in range(sums//2, -1, -1):
    if(dp[n][i]):
        ans = sums - i
        break
print(ans)







