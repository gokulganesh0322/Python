# 1 . Create a dictionary with keys name, age, and status. Print the dictionary.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026}
# print(dictionary)


# 2 . Create a dictionary that contains duplicate keys. Print the dictionary and observe the result.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "class":"sql",
# "batch":2026}
# print(dictionary)

# Result: Added the Duplicate Value to print the code given the output to latest version.


# 3 . Find and print the length of a dictionary.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026}
# print(len(dictionary))


# 4 . Print the data type of a dictionary.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026}
# print(type(dictionary))


# 5 . Convert a list into a set and print the result.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# a=list(dictionary)
# print(a)


# 6 . Create a dictionary using the dict() constructor.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# print(dict(dictionary))


# 7 . Access a value from a dictionary using the get() method.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# a=dictionary.get("name")
# print(a)


# 8 . Access a value from a dictionary using square brackets.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# print(dictionary.values())


# 9 . Check whether a specific key exists in a dictionary using the in operator.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# key="age"
# print(key in dictionary)

# key="year"
# print(key in dictionary)


# 10 . Add a new key-value pair to an existing dictionary.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# dictionary.update({"status":"live"})
# print(dictionary)


# 11 . Modify the value of an existing key in a dictionary.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# dictionary["class"]="SQL"
# print(dictionary)


# 12 . Remove a key from a dictionary using the del keyword.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# del(dictionary["name"])
# print(dictionary)


# 13 . Remove a specific key from a dictionary using the pop() method.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# dictionary.pop("class")
# print(dictionary)


# 14 . Remove the last inserted item from a dictionary using popitem().

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# dictionary.popitem()
# print(dictionary)


# 15 . Clear all elements from a dictionary.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# dictionary.clear()
# print(dictionary)


# 16 . Make a copy of a dictionary and print both dictionaries.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# co_dictionary=dictionary.copy()
# print(co_dictionary)


# 17 . Modify the original dictionary after copying it and compare both dictionaries.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"SQL",
# "batch":2026
# }
# co_dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# print(dictionary==co_dictionary)



# 18 . Loop through a dictionary and print only the keys.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# for keys in dictionary.keys():
#     print(keys)


# 19 . Loop through a dictionary and print only the values.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# for val in dictionary.values():
#     print(val)


# 20 . Loop through a dictionary and print key-value pairs using the items() method.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# for a in dictionary.items():
#     print(a)


# 21 . Print all keys using the keys() method.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# print(dictionary.keys())


# 22 . Print all values using the values() method.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# print(dictionary.values())


# 23 . Print all key-value pairs using the items() method.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# print(dictionary.items())


# 24 . Update a dictionary using the update() method.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# dictionary.update({"status":"live"})
# print(dictionary)


# 25 . Create a dictionary, clear it, and print the empty dictionary.

# dictionary={
# "name":"gokul",
# "age": 23,
# "class":"python",
# "batch":2026
# }
# dictionary.clear()
# print(dictionary)