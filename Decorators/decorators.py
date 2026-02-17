# def user():
#     print("Helooooooooooooooooo")
# user()

# In Python, decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code.

# A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.


# It returns a new function (wrapper) that first prints a message, calls greet() and then prints another message.


# def decorator(func):
#     def wrapper():
#         print("Before Calling")
#         func()
#         print("After Calling")
#     return wrapper





# def greet():
#     print("Hello World...")
# greet()

# @decorator
# def greeting():
#     print("........................................")
# greeting()