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

BotScoreData = namedtuple('name', 'num_moves', 'num_collisions', 'score')

# # Named Tuple
# clothes = [('t-shirt', 'green', 'large', 9.99),
#            ('jeans', 'blue', 'medium', 14.99),
#            ('jacket', 'black', 'x-large', 19.99),
#            ('t-shirt', 'grey', 'small', 8.99),
#            ('shoes', 'white', '12', 24.99),
#            ('t-shirt', 'grey', 'small', 8.99)]
#
# ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])
#
# new_coat = ClothingItem('coat', 'black', 'small', 14.99)
# print(new_coat)  # Prints ClothingItem(type='coat', color='black', size='small', price=14.99)
#
# coat_cost = new_coat.price
# print(coat_cost)  # Prints 14.99
#
# updated_clothes_data = []
#
# for item in clothes:
#     updated_clothes_data.append(ClothingItem(item[0], item[1], item[2], item[3]))
#
# print(updated_clothes_data)  # Prints [ClothingItem(type='t-shirt', color='green', size='large', price=9.99), ClothingItem(type='jeans', color='blue', size='medium', price=14.99), ClothingItem(type='jacket', color='black', size='x-large', price=19.99), ClothingItem(type='t-shirt', color='grey', size='small', price=8.99), ClothingItem(type='shoes', color='white', size='12', price=24.99), ClothingItem(type='t-shirt', color='grey', size='small', price=8.99)]

