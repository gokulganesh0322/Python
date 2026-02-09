# *# Scope of Variables:

# # 1. Global Scope
# # 2. Local Scope
# # 3. Non Local Scope



# def greet():
#     global x 
#     x = 100
#     print(x)
# greet()

# print(x)



# # 3. Non Local Scope

# def outerfunction():
#     message = "Original Function"


#     def innerfunction():
#         nonlocal message
#         message = "Modified Function "
#         # print(message)


#     innerfunction()
#     print(message)


# outerfunction()

