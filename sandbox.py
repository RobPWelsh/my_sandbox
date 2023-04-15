# Chat GPT explanations
# super().__init__()
class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent class constructor called.")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("Child class constructor called.")


child = Child("John", 10)
print(child.name)
print(child.age)
print('')


# Decorators
def log_function(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function", func.__name__, "returned", result)
        return result

    return wrapper


@log_function
def add_numbers(a, b):
    return a + b


result = add_numbers(3, 4)
print("Result:", result)


def solution(string):
    rev_string = ''
    n = -1
    for letter in string:
        rev_string = rev_string + string[n]
        n -= 1
    return rev_string


print(solution('World'))
