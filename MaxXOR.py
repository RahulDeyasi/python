def maxXOR(arr):
    n=len(arr)
    maxm=0
    for i in range(n):
        for j in range(n):
            maxm=max(maxm,arr[i] ^ arr [j])
    return maxm
arr=list(map(int,input().split()))
print(maxXOR(arr))
