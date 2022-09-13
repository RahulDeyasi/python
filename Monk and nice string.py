n=int(input())

arr=[]

for i in range(n):
    arr.append(input())
for i in range(n):
    count=0
    for j in range(i):
        if arr[j]<arr[i]:
            count+=1
    print(count)
