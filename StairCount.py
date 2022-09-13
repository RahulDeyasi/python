'''def countStairWay(n):
    memo={}
    if n==0:
        return 1
    if n<0:
        return 0
    if n in memo:
        return memo[n]
    else:
        memo[n]=countStairWay(n-1) + countStairWay(n-2)+ countStairWay(n-3)
    return memo[n]

n=int(input())
print(countStairWay(n))'''

def countStairWay(n):
    dp=[0 for i in range(n+1)]
    dp[0]=1
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]
n=int(input())
print(countStairWay(n))

    
