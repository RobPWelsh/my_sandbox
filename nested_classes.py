"""
From ChatGPT: The nested class InnerClass can access the variables and methods of the
OuterClass using the self keyword. Here's an example:
"""


class OuterClass:
    def __init__(self):
        self.outer_var = "Outer Variable"

    class InnerClass:
        def access_outer_var(self, outer_obj):
            print(outer_obj.outer_var)


outer_obj = OuterClass()
inner_obj = OuterClass.InnerClass()
inner_obj.access_outer_var(outer_obj)  # Output: Outer Variable

"""
In the above example, InnerClass is able to access the variable outer_var of OuterClass 
by passing an instance of OuterClass as an argument to the access_outer_var() method of InnerClass.
"""
