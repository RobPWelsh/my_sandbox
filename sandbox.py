from collections import Counter, deque

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

deque_z = deque(z)

print(deque_z)

num_blue = (Counter(deque_z)['blue'])

print(num_blue)




