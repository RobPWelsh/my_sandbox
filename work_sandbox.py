# This is the sandbox I'll use at work. First added to GitHub in the work_edits branch.
import ctypes
from enum import Enum, IntEnum
import numpy as np
import matplotlib.pyplot as plt
from ctypes import *

"""
class SourceType(Enum):
    VOLTAGE = 0,
    CURRENT = 1


class Source:
    def __init__(self, source_type):
        self.name = {SourceType.VOLTAGE: 'VoltageSource', SourceType.CURRENT: 'CurrentSource'}[source_type]


new_source = Source(SourceType.VOLTAGE)

print(new_source.name)  # VoltageSource

print(SourceType.VOLTAGE)  # SourceType.VOLTAGE
print(SourceType.VOLTAGE.value)  # (0,)
print(SourceType.VOLTAGE.name)  # VOLTAGE


# __________________________________________________
class Test:
    def __init__(self, channel):
        self.channel = channel
        if self.channel == 0:
            self.name = 'This is Channel 0'
        elif self.channel == 1:
            self.name = 'This is Channel 1'


# create a list of Test objects
voltage_input = []
voltage_input.append(Test(0))
voltage_input.append(Test(1))

print(voltage_input[0].channel)
print(voltage_input[1].channel)
print(voltage_input[0].name)
print(voltage_input[1].name)


# _____________________________________________
class Language1(IntEnum):
    CSharp = 1
    Go = 2
    VisualBasic = 3


class Language2(Enum):
    Python = 1
    Java = 2


# IntEnum
print(Language1.CSharp)  # 1
print(Language1.CSharp.value)  # 1

# Enum
print(Language2.Python)  # Language2.Python
print(Language2.Python.value)  # 1

# Passing an object into a function and use of __str__
def print_name(person):
    print(f"The person's name is {person.name}, and his age is {person.age}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


person1 = Person("Rob", 59)
print_name(person1)  # The person's name is Rob, and his age is 59

print(str(person1))  # Rob 59
print(person1)  # Rob 59

# Convert list to string using .join and list comprehension
data_sources = [('MDC', 1), ('MSET', 1)]
elements = ','.join(f'{mnemonic},{index}' for (mnemonic, index) in data_sources)
print(elements)  # MDC,1,MSET,1

# ______________________________________________________________________________
# Linear regression: y = mx + b

# x_values = [1, 2, 3, 4, 5, 6, 7]
# y_values = [1.5, 5, 6.7, 9.8, 11.2, 12.1, 16]
#
# fit_eq = np.polyfit(x_values, y_values, 1)  # returns m and x
#
# print(fit_eq)  # [2.22142857 0.01428571]
#
# fitted_y = [x * fit_eq[0] + fit_eq[1] for x in x_values]
#
# plt.scatter(x_values, y_values, color='DarkOrange')
# plt.plot(x_values, fitted_y, color='Blue')
# plt.show()

"""
colors = ['Red', 'White', 'Blue', 'Green']
for color in colors:
    print(color)
    something = input("Enter something: ")
    print(something)





