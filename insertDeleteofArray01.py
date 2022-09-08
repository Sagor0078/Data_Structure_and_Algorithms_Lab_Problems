

def insert(arr,key):
    arr.append(key)

arr = [1,2,3,4,5,6,7,8,9]
key = 5
insert(arr,key)
# inserting key
print(arr)
remove_key = 7
#remove key
arr.remove(remove_key)
print(arr)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
# [1, 2, 3, 4, 5, 6, 8, 9, 5]