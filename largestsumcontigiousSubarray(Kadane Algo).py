maxint=10000
def maxSubarray(arr,n):
    max_so_far=-maxint -1
    max_end_here=0
    for i in range(n):
        max_end_here=max_end_here + arr[i]
        if max_so_far<max_end_here:
            max_so_far=max_end_here
        if max_end_here<0:
            max_end_here=0
    return max_so_far
arr= list(map(int, input().split() ))
n=len(arr)
print(maxSubarray(arr,n))
