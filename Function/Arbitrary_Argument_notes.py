# Arbitrary Arguments
# In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments
#  to a function using special symbols. There are two special symbols:

# # *args in Python (Non-Keyword Arguments)
# *args allows a function to accept any number of non-keyword (positional) arguments. 
# Inside the function, these arguments are collected into a tuple. 



# def sum(*mynumbers):
#     result = 0
#     for i in mynumbers:
#         result = result + i
#     print(result)        
# sum(9,100, 4, 5, 6, 7, 8, 9, 9)




# **kwargs in Python (Keyword Arguments)
# In Python, **kwargs is a special syntax used in a function definition
#  to accept a variable number of keyword arguments (arguments passed as key=value pairs).
#  Inside the function, these arguments are collected into a dictionary, 
# where the keys are the argument names and the values are the corresponding values. 
# def mynames(**name):
#     for key, values in name.items():
#         print(f"{key} - {values}")

# mynames(name="Alice", age=30, city="Paris", hobby="coding")