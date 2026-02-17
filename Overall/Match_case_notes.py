# The match statement, introduced in Python 3.10, provides a powerful mechanism for structural pattern matching, offering a more expressive and readable alternative to long if/elif/else chains. It compares a value (the subject) against a series of patterns and executes the code block of the first matching pattern



# Syntax
# match subject:
#     case pattern_1:
#         # Code block 1
#     case pattern_2:
#         # Code block 2
#     # ...
#     case _:
#         # Default code block (wildcard)



# myletter = "A"
# match myletter:
#     case "B":
#         print("Its B")
#     case "C":
#         print("Its C")
#     # case "A":
#     #     print("Pattern matched")
#     case _:
#         print("None is Matched")

# status = 400097
# match status:
#     case 200 | 201:
#         print("Success") 
#     case 400 | 404:
#        print("Client error")
#     case _:
#         print("None is Matched")