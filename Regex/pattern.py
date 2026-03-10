# Regular Expression (Regex) is a sequence of characters that defines a search pattern used to match,
#  validate, extract, or manipulate text data.

# In Python, a "full match" in a regular expression refers to the scenario where the entire target string,
#  from the first character to the last, matches the given pattern.


# Patterns

# name_pattern = r"^[A-Za-z ]{3,30}$"
# roll_pattern = r"^STU\d{4}$"
# course_pattern = r"^[A-Z]{2}\d{3}$"
# email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
# mobile_pattern = r"^[6-9]\d{9}$"

import re

# -------- REGEX PATTERNS --------
# name_pattern = r"^[A-Za-z ]{3,30}$"
# roll_pattern = r"^STU\d{4}$"
# course_pattern = r"^[A-Z]{2}\d{3}$"
# email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
# mobile_pattern = r"^[6-9]\d{9}$"


# # -------- INPUTS --------
# name = input("Enter Student Name: ")
# roll = input("Enter Roll Number (STU1234): ")
# course = input("Enter Course Code (CS101): ")
# email = input("Enter Email: ")
# mobile = input("Enter Mobile Number: ")


# # -------- VALIDATION FUNCTION --------
# def validate(pattern, value):
#     return re.fullmatch(pattern, value) is not None




# print("Name Valid:", validate(name_pattern, name))
# print("Roll Number Valid:", validate(roll_pattern, roll))
# print("Course Code Valid:", validate(course_pattern, course))
# print("Email Valid:", validate(email_pattern, email))
# print("Mobile Valid:", validate(mobile_pattern, mobile))




name_pattern = r"^[A-Za-z ]{3,30}$"
roll_pattern = r"^[2]\d{10}$"
course_pattern = r"^[A-Z.]{1,}$"
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
mobile_pattern = r"^[6-9]\d{9}$"


# -------- INPUTS --------
name = input("Enter Student Name: ")
roll = input("Enter Roll Number : ")
course = input("Enter Course : ")
email = input("Enter Email: ")
mobile = input("Enter Mobile Number: ")


# -------- VALIDATION FUNCTION --------
def validate(pattern, value):
    return re.fullmatch(pattern, value) is not None




print("Name Valid:", validate(name_pattern, name))
print("Roll Number Valid:", validate(roll_pattern, roll))
print("Course Valid:", validate(course_pattern, course))
print("Email Valid:", validate(email_pattern, email))
print("Mobile Valid:", validate(mobile_pattern, mobile))