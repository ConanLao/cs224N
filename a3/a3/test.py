a = [1,2,3]
print(f'a = {a}')
b = a
print(b)
a[0] = 11
print(b)

from collections import deque

a = deque([1,2,3])
print(a[0])
print(a[1])
print(a[2])
# while a:
#     print(f'{a.popleft()}')