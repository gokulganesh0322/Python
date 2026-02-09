# 1 . Write a program that checks whether a number entered by the user is *positive or negative* using if–else.

# corona_Test=int(input("Enter your Temperature: ", ))

# if corona_Test >= 40:
#     print("Positive")
# else:
#     print("Nagative") 


# 2 . Write a program to check whether a given number is *even or odd* using if–else.

# number=int(input("Enter the number: ", ))
# if (number % 2) == 0:
#     print("this is even number")
# else:
#     print("this is odd number")


# 3 . Write a program that checks whether a person is *eligible to vote* based on age using if–else.

# age=int(input("Enter your age: ", ))

# if age >= 18:
#     print("eligible")
# else:
#     print("Not eligible")


# 4 . Write a program to find the *largest of two numbers* using if–else.

# num1=int(input("Enter your number: " ))
# num2=int(input("Enter your number: " ))

# if num1 > num2:
#     print("{0} Greater than {1}".format(num1,num2))
# elif num2 > num1:
#     print ("{0} Greater than {1}".format(num2,num1))
# else:
#     print("Both num1 and num2 are equal")


# 5 . Write a program to find the *largest of three numbers* using *nested if*.

# num1=int(input("Enter your number: " ))
# num2=int(input("Enter your number: " ))
# num3=int(input("Enter your number: " ))

# if num1 > num2:
#     if num1 > num3:
#         g = num1
#     else:
#         g > num3
# else:
#     if num2 > num3:
#         g = num2
#     else:
#         g = num3
# print("greater = ", g)


# 6. Write a program that checks a student’s *grade* based on marks using *nested if*
#    (e.g., A, B, C, Fail).

# mark=int(input("Enter your number:" ))

# if mark >= 90:
#     print("Grade A")
# else:
#     if mark >= 70:
#         print("Grade B")
#     else:
#         if mark >= 35:
#             print("Grade C")
#         else:
#             print("fail")


# 7. Write a program using *match–case* that prints the *day of the week* based on a number (1–7).

# day=int(input("Enter the number"))
# match day:

#     case 0:
#         print("sunday")

#     case 1:
#         print("Monday")

#     case 2:
#         print("Tuesday")

#     case 3:
#         print("Wennesday")

#     case 4:
#         print("Thusday")

#     case 5:
#         print("Friday")

#     case 6:
#         print("saturday")

#     case _:
#         print("Enter no. between 0-6")


# 8 . Write a program using *match–case* to perform a simple *calculator operation*
#    (addition, subtraction, multiplication, division).

# a=int(input("Enter the number"))
# b=int(input("Enter the number"))
# c= input("Enter operator (+, -, *, /): ")

# match c:

#     case "+":
#         print(f"{a} {c} {b} = {a+b}")
#     case "-":
#         print(f"{a} {c} {b} = {a-b}")
#     case "*":
#         print(f"{a} {c} {b} = {a*b}")
#     case "/":
#         print(f"{a} {c} {b} = {a/b}")
#     case _:
#         print("invalid input")

