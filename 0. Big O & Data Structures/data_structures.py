from collections import deque, Counter
import math

# Stack: LIFO, use a python list - theoretical implementation is with a single pointer, pointing at the top of the stack (next unused space)
# pushing involves setting the value at the pointer to the item and increment the pointer by 1. Decrease the pointer by 1 to pop (no need to reset the item)

# Queue: FIFO, use a python list - theoretical implementation is with two pointers, pointing to start & end of queue
# Deque, use (from collections import deque)  a double ended queue where one can interact with both ends - peeking, popping & pushing from both ends
# theoretical implementation involves the increment and decrement of both start & end pointers
q = deque()
q.append(5)
q.append(10)
q.popleft()  # remove element from front of queue

# Note these theoretical implementations use fixed sized arrays (so lists are better as they dynamically grow as they need more memory)

# note modifying a list in place helps with space complexity (as no new space is used)
orig_list = [2, 4, 6, 8]
orig_list[::] = orig_list[3:] + orig_list[:3]

# Hash function -> converts data of arbitrary size to value of fixed size (this is the hash value - usually 32-bit integer)
# Hash map -> data stored in a fix-sized array, where the key is hashed to generate a value within the range of the array
# to retrieve, the key is hashed and returns the index in the array containing the value
# counter can accept an iterable and return a dictionary of each hashable object - length will be unique elements in iterable
lst = [1, 2, 1, 1, 1, 2, 4, 5, 4, 4, 6]
print(Counter(lst))
print(len(Counter(lst)))

# represent infinity
positive_inf = math.inf
negative_inf = -math.inf
