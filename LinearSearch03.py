
#author : Sagor
def linear_search(arr,n,x):
    for i in range(0,n):
        if(arr[i] == x):
            return i
    return -1
arr = list(map(int,input().split()))
x = int(input())
n = len(arr)
result = linear_search(arr,n,x)
if result == -1:
    print("Not found")
else:
    print("found at index :",result)