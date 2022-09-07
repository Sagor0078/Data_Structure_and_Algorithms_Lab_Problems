
#https://www.geeksforgeeks.org/queue-in-python/
# Python program to
# demonstrate queue implementation
# using list

# Initializing a queue
queue = []
# Adding elements to the queue
queue.append('1')
queue.append('2')
queue.append('3')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty
