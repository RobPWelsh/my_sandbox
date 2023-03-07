# Without __init__.py file in the Support_files directory

# from Support_files.object_one import ClassOne
# from Support_files.object_two import ClassTwo
#
# x = ClassOne()  # Prints This is something from ClassOne
# y = ClassTwo()  # Prints This is something from ClassTwo

# __________________________________________________________

# With __init__.py file in the Support_files directory

# import Support_files
#
# x = Support_files.ClassOne()  # Prints This is something from ClassOne
# y = Support_files.ClassTwo()  # Prints This is something from ClassTwo

# __________________________________________________

# The import can also be structured this way (with the __init__.py file)

from Support_files import ClassOne
from Support_files import ClassTwo

x = ClassOne()  # Prints This is something from ClassOne
y = ClassTwo()  # Prints This is something from ClassTwo

# Add note to test push to GitHub from work account.
