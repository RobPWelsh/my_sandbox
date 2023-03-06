guests = {'Tim': 22, 'Tonya': 45, 'Mary': 12, 'Ann': 32, 'Beth': 20, 'Sam': 5, 'Manny': 76, 'Kenton': 15, 'Kenny': 27, 'Dixie': 46, 'Jane': 35, 'Mallory': 32, 'Julian': 4, 'Edward': 71, 'Rose': 65}

for x in guests:
    print(x)  # Prints each name (key) on a separate line

for x in guests:
    print(guests[x])  # Prints each age (value) on a separate line

for x, y in guests.items():
    print(x, y)  # prints each name and age (key and value) on a separate line

print(' ')
# Another example

student = {'name': 'John', 'Age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

for x in student:
    print(x)

for x in student:
    print(student[x])

for x, y in student.items():
    print(x, y)

