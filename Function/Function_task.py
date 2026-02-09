# 1 . Write a function named greet() that prints "Hello, Welcome to Python!". Call the function.

# def greet(hello):
#     print(f"Welcome to python",hello)


# greet("hello")


# 2 . Write a function say_hello(name) that takes one parameter name and prints "Hello, <name>".

# def say_hello(name):
#     print("Hello, " + name)


# say_hello("Gokul")


# 3 . Create a function add_numbers(a, b) that accepts two parameters and returns their sum. Print the returned value.

# def add_number(a,b):
#     print(a+b)

# add_number(1,2)


# 4 . Write a function calculate_area(length, width) that returns the area of a rectangle. Call the function using positional arguments.

# def calculate_area(length, width):
#     return length * width

# # Calling the function using positional arguments
# area = calculate_area(5, 10)
# print("Area of the rectangle:", area)


# Create a function power(base, exponent=2) that returns the value of base raised to the power of exponent. 
# Call the function once with default argument and once by passing both arguments.

# def function_power(base,exponent=2):
#     return base ** exponent

# area = function_power(4)
# print("values:",area)

# area1 = function_power(4,3)
# print("passing both argument:", area1)


# 6. Write a function student_info(name, age, course) that prints student details. 
# Call the function using keyword arguments in any order.


# def student_info(name, age, course):
#     print("Name:", name)
#     print("Age:", age)
#     print("Course:", course)

# # Calling the function using keyword arguments (any order)
# student_info(course="m.com", name="Gokul", age=23)


# 7 . Create a function calculate_salary(basic_salary, bonus=2000) that returns the total salary.
# Call the function once with only basic_salary and once with both arguments.

# def calculate_salary(basic_salary, bonus=2000):
#     return basic_salary + bonus
# total1=calculate_salary(22000)
# print("total salary with defult bonus:", total1)

# total2=calculate_salary(22000,2000)
# print("Total salary with custom bonus:", total2)


# calculate_salary(basic_salary=22000,bonus=2000)


# 8 . Write a function book_ticket(movie, seats, price=150) that returns the total ticket cost.
# Call the function using positional arguments and keyword arguments.

# def book_ticket(movie, seats, price=150):
#     return seats * price

# # Calling the function using positional arguments
# cost1 = book_ticket("Inception", 3)
# print("Total ticket cost (positional arguments):", cost1)

# # Calling the function using keyword arguments
# cost2 = book_ticket(movie="Inception", seats=3, price=150)
# print("Total ticket cost (keyword arguments):", cost2)


# 9. Create a function math_operations(a, b) that returns sum, difference, and multiplication of the two numbers. 
# Capture and print all returned values.

# def math_operations(a, b):
#     total = a + b
#     difference = a - b
#     multiplication = a * b
#     return total, difference, multiplication

# # Calling the function and capturing all returned values
# sum_result, diff_result, mul_result = math_operations(10, 5)

# print("Sum:", sum_result)
# print("Difference:", diff_result)
# print("Multiplication:", mul_result)


# 10 . Write a function login(username, password, otp=None). If otp is provided, print "Login successful with OTP"; otherwise, print "Login successful".
# Call the function with and without otp.

# def login(username, password, otp=None):
#     if otp is not None:
#         print("Login successful with OTP")
#     else:
#         print("Login successful")

# # Call without OTP
# login("gokul", "password123")

# # Call with OTP
# login("gokul", "password123", otp=456789)