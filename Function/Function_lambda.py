# # The return keyword in Python is used within a function to stop its execution and send a value back to the caller. 


# def greet():
#     print("ikutefuyt")
#     return "Hello"
#     print("wrfu7byig")


# print(greet())


# Pass Keyword - The pass keyword in Python is a null statement that serves as a placeholder where code is syntactically required but no action needs to be executed


# Recursion in Python is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, simpler subproblems

# Key Components of a Recursive Function

# 1.) Base Case: This is the condition that stops the recursion. It is a simple case that can be solved directly without any further function calls.

# 2.)Recursive Case: This is the part of the function that calls itself with a modified (usually smaller or simpler) input, moving the problem closer to the base case. 


# def factorial(n):
# #    Base Case
#    if n == 0:
#       return 1
# #    Recursive Case
#    else:
#       return n * factorial(n - 1)

# print(factorial(10))
    


# Lambda Functions: Also known as anonymous functions, these are small, single-expression functions defined using the lambda keyword. They can take any number of arguments but can only have one expression


# User Defined Function
# num = int(input("Please Enter a Value to Square: "))
# def squared(n):
#     print(n ** 2)
# squared(num)


# lambda Function:
# squared = lambda x : x **2
# print(squared(6))

# greet = lambda name: name
# print("Hello World")