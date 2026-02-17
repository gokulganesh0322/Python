# # Python Exception Handling allows a program to gracefully handle unexpected events
#  (like invalid input or missing files) without crashing. Instead of terminating abruptly,
#  Python lets you detect the problem, respond to it, and continue execution when possible.

# # try: Runs the risky code that might cause an error.

# # except: Catches and handles the error if one occurs.


# a = 10
# b = 2


# try:
#     print(a/b)
# except:
#     print("This is a error statement")


# print("Hellooo")


# else: Executes only if no exception occurs in try.


# a = 10
# b = 2
# try:
#    output = a/b
# except:
#     print("This is a error statement")
# else:
#     print(f"{output} My code working good")
    


# finally : The finally block will always be executed, no matter if the try block raises an error or not:   - This can be useful to close objects and clean up resources.

# a = 10
# b = 0
# try:
#    output = a/b
# except:
#     print("This is a error statement")
# else:
#     print(f"{output} My code working good")
# finally:
#     print("My Exception Hadnling Process is completed")