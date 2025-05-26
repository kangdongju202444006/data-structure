from collections import deque

d = deque([91,17,33])
d.append(-14)
d.appendleft(100)
d.append(99) #enqueue
print(d.popleft()) #dequeue
print(d.popleft())