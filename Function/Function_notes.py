# # Formatted String
# name = "John"
# print("Good Morning",name)
# print(f"Good Morning {name}")



# Functions in Python
# def greetings(name):
#     print(f"Good Morning: {name}")


# greetings("Gokul")
# greetings("Bose")
# greetings("Maariosn")
# greetings("kuged fuye3f")
# greetings("kuytfuyb")


# Parameters are variables defined in a function declaration. This act as placeholders for the values (arguments) that will be passed to the function.

# Arguments are the actual values that you pass to the function when you call it. These values replace the parameters defined in the function.


# Positional Arguments are needed to be included in proper order i.e the first argument is always listed first when the function is called, second argument needs to be called second and so on.


# Keyword Arguments is an argument passed to a function or method which is preceded by a keyword and equal to sign (=). The order of keyword argument with respect to another keyword argument does not matter because the values are being explicitly assigned.



# def add(a,b):
#     print(a + b)

# # add(10,20)
# # add(100,20)

# add(b = 10,a = 67)



# Positional Arguments and Keyword Arguements


# # Positional Arguemnst
# def greet(firstname, lastname):
#     print(f"Hi My name is {firstname} {lastname}")

# greet("Santhosh", "Kumar")
# greet("Kumar", "Santhosh")


# # Keyword Arguements
# greet(lastname="Kumar", firstname="Santhosh")



# Default Arguements
# def add(a,b=100):
#     print(a + b)


# add(10)






def name(firstname , middlename, lastname):
    print(f"my full name is: {firstname} {middlename} {lastname}")

name("dhoni","ms","singh")

name(lastname="dhoni" ,middlename="singh",firstname="ms")