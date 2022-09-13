t=int(input())
while t>0:
    n=int(input())
    h=list(map(int,input().split()))
    h.sort()
    print(h)
    t-=1
