# 1 . Write a ython program using a for loop to print numbers from 1 to 20. Use continue to skip numbers that are divisible by 3.

# for i in range(1,21,2):
#     print(i//3)


# 2. Write a Python program using a for loop to iterate through a list of numbers [5, 10, 15, 20, 25, 30]. Use break when the number is greater than 20.

# a=[5, 10, 15, 20, 25, 30]
# for i in a:
#     print(i)
#     if i == 20:
#         break


# 3. Write a Python program using a while loop to print numbers from 1 to 15. Use break when the number reaches 10.

# number=0
# while number <= 14:
#     number += 1
#     print(number)

#     if number == 10:
#         break


# 4 . Write a Python program using a while loop to print numbers from 1 to 20. Use continue to skip even numbers.

# number=0
# while number <= 19:
#     number += 1
#     if number % 2 == 1:
#         print(number)


# 5 . Write a Python program using a for loop to print all characters in the string "PYTHON". Use continue to skip the character 'T'.

# for i in "PYTHON":
#     if i == "T":
#         continue
#     print(i, end=" ")
        

# 6 . Write a Python program using a for loop to find the first number divisible by 7 between 1 and 50. Use break once the number is found.


# for num in range(1, 51):
#     if num % 7 == 0:
#         print("The first number divisible by 7 is:", num)
#         break


# 7 . Write a Python program using a while loop to print numbers from 10 down to 1. Use continue to skip the number 5.

    
# num = 10
# while num >= 1:
#     if num == 5:
#         num -= 1
#         continue
#     print(num)
#     num -= 1


# 8 . Write a Python program using a for loop to iterate through a list of integers [12, 25, 7, 30, 18, 5].
#  Use break when a number less than 10 is encountered.


# numbers = [12, 25, 7, 30, 18, 5]

# for i in numbers:
#     if i < 10:
#         break
#     print(i)


# 9 . Write a Python program using a while loop to continuously ask the user to enter a number. Stop the loop using break when the user enters 0.


# while True:
#     a=int(input("Enter the Number:" ))
#     if a == 0:
#         break
#     print("You entered:", a)


# 10 . Write a Python program using a for loop to print numbers from 1 to 30. Use continue to skip numbers that are multiples of 4.

# for i in range(1,31):
#     if i % 4 == 0:
#         continue
#     print(i)


