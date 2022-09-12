def merge(left,right):
  result = []
  i,j = 0, 0 
  while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        result.append(left[i])
        i+=1
      else:
        result.append(right[j])
        j+=1
  result += left[i:]
  result += right[j:]
  return result
       

def mergesort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left,right)



# n = int(input())
arr = [9,8,7,5,6,2,3,1]
print('sorted array : ')
print(mergesort(arr))
