from collections import Counter, deque

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

deque_z = deque(z)

print(deque_z)

num_blue = (Counter(deque_z)['blue'])

print(num_blue)

deque_moves = deque([('A', 'right', False), ('B', 'up', False), ('C', 'right', False), ('A', 'right', False),
                     ('B', 'right', True), ('C', 'down', True), ('A', 'right', True), ('B', 'right', False),
                     ('C', 'down', True), ('A', 'down', True), ('B', 'down', True), ('C', 'up', False),
                     ('A', 'right', True), ('B', 'down', False), ('C', 'down', True), ('A', 'right', False),
                     ('B', 'right', False), ('C', 'right', False), ('A', 'finished', True), ('B', 'right', True),
                     ('C', 'right', False), ('B', 'down', True), ('C', 'down', True), ('B', 'up', False),
                     ('C', 'right', False), ('B', 'down', True), ('C', 'right', False), ('B', 'right', False),
                     ('C', 'finished', True), ('B', 'right', False), ('B', 'finished', False)])

list_of_bots = []
for move in deque_moves:
    list_of_bots.append(move[0])

print(list_of_bots)

comp_list_of_bots = [move[0] for move in deque_moves]

print(comp_list_of_bots)

num_moves_a = Counter([move[0] for move in deque_moves])['A']
print(num_moves_a)

num_collision_a = Counter([move[2] for move in deque_moves if 'A' in move])[True]

print(num_collision_a)


