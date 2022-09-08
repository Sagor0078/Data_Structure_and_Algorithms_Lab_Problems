
#Author : Sagor
n = int(input())
a = list(map(int,input().split()))
for i in range(n-1):
    for j in range(1,n):
        if a[j-1] > a[j]:
            a[j-1],a[j] = a[j],a[j-1]
    print(i+1," step :",*a)
# 5
# 5 4 3 2 1
# 1  step : 4 3 2 1 5
# 2  step : 3 2 1 4 5
# 3  step : 2 1 3 4 5
# 4  step : 1 2 3 4 5