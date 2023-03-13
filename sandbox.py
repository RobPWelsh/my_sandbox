from collections import Counter, deque

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

deque_z = deque(z)

print(deque_z)

num_blue = (Counter(deque_z)['blue'])

print(num_blue)

deque_moves = deque([('A', 'right', False), ('B', 'up', False), ('C', 'right', False), ('A', 'right', False), ('B', 'right', True), ('C', 'down', True), ('A', 'right', True), ('B', 'right', False), ('C', 'down', True), ('A', 'down', True), ('B', 'down', True), ('C', 'up', False), ('A', 'right', True), ('B', 'down', False), ('C', 'down', True), ('A', 'right', False), ('B', 'right', False), ('C', 'right', False), ('A', 'finished', True), ('B', 'right', True), ('C', 'right', False), ('B', 'down', True), ('C', 'down', True), ('B', 'up', False), ('C', 'right', False), ('B', 'down', True), ('C', 'right', False), ('B', 'right', False), ('C', 'finished', True), ('B', 'right', False), ('B', 'finished', False)])

num_a = []
for move in deque_moves:
    num_a.append((Counter(move)['A']))
print(num_a)

num_A = sum([(Counter(move)['A']) for move in deque_moves])
print(num_A)

num_B = sum([(Counter(move)['B']) for move in deque_moves])
print(num_B)

num_C = sum([(Counter(move)['C']) for move in deque_moves])
print(num_C)
