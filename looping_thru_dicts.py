from collections import UserDict

# guests = {'Tim': 22, 'Tonya': 45, 'Mary': 12, 'Ann': 32, 'Beth': 20, 'Sam': 5, 'Manny': 76, 'Kenton': 15, 'Kenny': 27,
#           'Dixie': 46, 'Jane': 35, 'Mallory': 32, 'Julian': 4, 'Edward': 71, 'Rose': 65}
#
# for x in guests:
#     print(x)  # Prints each name (key) on a separate line
#
# for x in guests:
#     print(guests[x])  # Prints each age (value) on a separate line
#
# for x, y in guests.items():
#     print(x, y)  # prints each name and age (key and value) on a separate line
#
# print(' ')
# Another example

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}


class OrderProcessingDict(UserDict):

    def clean_orders(self):
        items_to_remove = []

        for key, value in self.data.items():
            if value['order_status'] == 'complete':
                items_to_remove.append(key)

        for item in items_to_remove:
            del self.data[item]


process_dict = OrderProcessingDict(data)

process_dict.clean_orders()

print(data)
