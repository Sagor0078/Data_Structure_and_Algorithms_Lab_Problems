
#author : Sagor

def binary_search(arr,item):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low<= high:
        mid = low + (high - low) // 2
        if item == arr[mid]:
            return mid
        if item < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

n = int(input())
arr = list(map(int,input().split()))
item = int(input())
result = binary_search(arr,item)
if result != -1:
    print(item,"found at position :",str(result))
else:
    print("Not found")