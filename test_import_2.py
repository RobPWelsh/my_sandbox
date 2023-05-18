# 1: Without __init__.py file in the Support_files_2 directory

# from support_files_2.support_file_1 import ClassOne
# from support_files_2.support_file_2 import ClassTwo
# from support_files_2.support_file_1 import function_one
# from support_files_2.support_file_2 import function_two
#
#
# x = ClassOne()  # Prints This is printed from ClassOne
# y = ClassTwo()  # Prints This is printed from ClassTwo
#
# a = function_one()
# print(a)  # Prints This is returned from function_one
# #
# b = function_two()
# print(b)  # Prints This is returned from function_two

# _________________________________________________________________________________________________
# 2: With __init__.py file in the Support_files directory, structured as:
'''
    from support_files_2.support_file_1 import ClassOne
    from support_files_2.support_file_2 import ClassTwo
    from support_files_2.support_file_1 import function_one
    from support_files_2.support_file_2 import function_two
'''

# import support_files_2
#
# x = support_files_2.ClassOne()  # Prints This is printed from ClassOne
# y = support_files_2.ClassTwo()  # Prints This is printed from ClassTwo
#
# a = support_files_2.function_one()
# print(a)  # Prints This is returned from function_one
#
# b = support_files_2.function_two()
# print(b)  # Prints This is returned from function_two

# ___________________________________________________________________________________________________
# 3: The import can also be structured this way (with the __init__.py file structured as 2 above)

# from support_files_2 import ClassOne
# from support_files_2 import ClassTwo
# from support_files_2 import function_one
# from support_files_2 import function_two
#
# x = ClassOne()  # Prints This is something from ClassOne
# y = ClassTwo()  # Prints This is something from ClassTwo
#
# a = function_one()
# print(a)  # Prints This is returned from function_one
#
# b = function_two()
# print(b)  # Prints This is returned from function_two

# ___________________________________________________________________________________________________
# 4: The following format works if the __init__.py is blank or it is structured as:
"""
    from support_files_2 import support_file_1
    from support_files_2 import support_file_2
"""
# from support_files_2 import support_file_1
# from support_files_2 import support_file_2
#
# x = support_file_1.ClassOne()  # This is printed from ClassOne
# y = support_file_2.ClassTwo()  # This is printed from ClassTwo
#
# a = support_file_1.function_one()
# print(a)  # Prints This is returned from function_one
#
# b = support_file_2.function_two()
# print(b)  # Prints This is returned from function_two

# __________________________________________________________________________________________________
# 5 The __init__.py structured as follows:
"""
    from .support_file_1 import *
    from .support_file_2 import *
"""
import support_files_2  # imports directory

x = support_files_2.ClassOne()  # This is printed from ClassOne
y = support_files_2.ClassTwo()  # This is printed from ClassTwo

a = support_files_2.function_one()
print(a)  # Prints This is returned from function_one

b = support_files_2.function_two()
print(b)  # Prints This is returned from function_two
