# 1. Write a function that uses `*args` to print all numbers passed to it.

# def add(*num):
#     c=0
#     for i in num:
#         c += i
#     print(f"Sum is {c}")

# add(1,2,3,4,5,6,)
# add(5,6,9,8,7,5,5,)


# 2. Write a function that uses `*args` to find the largest number.

# def num(*args):
#     num1 = args[0]
#     for i in args:
#         if i > num1:
#             num1 = i
#     return num1
# print(num(5,8,9,6,3,4))

# 3. Write a function that uses `*args` to count how many values were passed.

# def num(*args):
#     return len(args)
# print(num(5,9,6,3,5,6,8))


# 4. Write a function that uses `*args` to return all arguments as a list.

# def num(*args):
#     return list(args)
# print(num(45,6,9,4,3,5,7))


# 5. Write a function that uses `**kwargs` to print all keys and values.

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_kwargs(name="Gokul", age=22, city="Chennai")


# 6. Write a function that uses `**kwargs` to return only the keys.

# def get_keys(**kwargs):
#     return list(kwargs.keys())

# result = get_keys(name="Gokul", age=22, city="Chennai")
# print(result)


# 7. Write a function that uses `**kwargs` to return only the values.

# def get_keys(**kwargs):
#     return list(kwargs.values())

# result = get_keys(name="Gokul", age=22, city="Chennai")
# print(result)


# 8. Write a function that uses `**kwargs` to check if a specific key exists.

# def key_exists(key_to_check, **kwargs):
#     return key_to_check in kwargs

# # Example call
# result = key_exists("age", name="Gokul", age=22, city="Chennai")
# print(result)


# 9. Write a function that uses both `*args` and `**kwargs` and prints them separately.

# def get_keys(**kwargs):
#     return list(kwargs.items())

# result = get_keys(name="Gokul", age=22, city="Chennai")
# print(result)


# def args_kwargs(*args, **kwargs):
#     print("Positional arguments (*args):")
#     for i in args:
#         print(i)

#     print("\nKeyword arguments (**kwargs):")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# args_kwargs(10, 20, 30, name="Gokul", city="Chennai", age=22)


# 10. Write a function that uses `*args` for names and `**kwargs` for ages and prints them.

# def print_names_ages(*names, **ages):
#     print("Names:")
#     for name in names:
#         print(name)

#     print("\nAges:")
#     for person, age in ages.items():
#         print(f"{person}: {age}")

# print_names_ages("Gokul", "gokulraj", "dass", Gokul=24, gokulraj=21, dass=23)




