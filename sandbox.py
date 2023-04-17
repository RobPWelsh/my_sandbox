# import tkinter as tk
# from tkinter import ttk
import sys
from enum import Enum, IntEnum
import logging

#
# def popup_message(title_text, message_text, confirmation_button_text):
#     normal_font = ('Helvetica', 16)
#     popup = tk.Tk()
#     popup.attributes("-topmost", True)
#     popup.wm_title(title_text)
#     label = ttk.Label(popup, text=message_text, font=normal_font)
#     label.pack(side="top", fill="both", padx=60, pady=60)
#     B1 = ttk.Button(popup, text=confirmation_button_text, command=popup.destroy, padding=10)
#     B1.pack(side="bottom", pady=20)
#     popup.mainloop()
#
#
# popup_message('Manual step',
#               'Connect BNC adapter cable to Triton head',
#               'Cable connected')

# ______________________________________________________________
# enumerate function
my_list = ['rob', 'paul', 'welsh']

for count, value in enumerate(my_list):
    print(count, value)


# __________________________________________________________________
# Enum class

class Color(str, Enum):
    RED = 'one'
    GREEN = 'two'
    BLUE = 'three'

    # Gets around having to use .value to access the string
    def __str__(self) -> str:
        return str.__str__(self)


print(Color.RED.name)  # RED
print(Color.RED.value)  # one
print(Color.RED)  # one (__str__ method gets around having to use .value)


# _____________________________________________________
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


