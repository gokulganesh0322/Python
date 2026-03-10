# from pymongo import MongoClient

# # Creating a Connection
# cleint = MongoClient("mongodb://localhost:27017/")


# # Creating a DataBase
# DB = cleint["MyDataBase"]

# # Creating a Collection
# collection = DB["Mystudents"]

# print("MongoDB Connected Successfully")


# data = {
#     "name": "Maarison",
#     "course": "Python Full Stack"
# }



# Method to insert a Data in Mongo Db Compass
# insert_one() is a PyMongo method used to insert a single document into a MongoDB collection.

# collection.insert_one(data)
# print("data Inserted Successfully")

# Insert multiple documents

# many_data = [
#     {"name": "Bob", "department": "Engineering"},
#     {"name": "Charlie", "department": "Marketing"}
# ]

# collection.insert_many(many_data)
# print("Data Inserted Successfully")


# Find a document
# find_document = collection.find_one({"name": "Bob"})
# print(find_document)


# Delete a document
# delete_result = collection.delete_one({"name" : "Charlie"})
# print("data deleted successfully")



# from pymongo import MongoClient

# # Creating a Connection
# cleint = MongoClient("mongodb://localhost:27017/")


# # Creating a DataBase
# DB = cleint["MyDataBase"]

# # Creating a Collection
# collection = DB["Mystudents"]

# print("MongoDB Connected Successfully")


# data = {
#     "name": "Maarison",
#     "course": "Python Full Stack"
# }


# users = [
#     {"name": "Arun", "age": 23, "email": "arun23@gmail.com", "password": "pass123"},
#     {"name": "Priya", "age": 25, "email": "priya25@gmail.com", "password": "pass123"},
#     {"name": "Rahul", "age": 22, "email": "rahul22@gmail.com", "password": "pass123"},
#     {"name": "Sneha", "age": 24, "email": "sneha24@gmail.com", "password": "pass123"},
#     {"name": "Karthik", "age": 26, "email": "karthik26@gmail.com", "password": "pass123"},
#     {"name": "Divya", "age": 23, "email": "divya23@gmail.com", "password": "pass123"},
#     {"name": "Vikram", "age": 27, "email": "vikram27@gmail.com", "password": "pass123"},
#     {"name": "Anjali", "age": 21, "email": "anjali21@gmail.com", "password": "pass123"},
#     {"name": "Rohit", "age": 28, "email": "rohit28@gmail.com", "password": "pass123"},
#     {"name": "Meera", "age": 22, "email": "meera22@gmail.com", "password": "pass123"},
#     {"name": "Suresh", "age": 29, "email": "suresh29@gmail.com", "password": "pass123"},
#     {"name": "Lakshmi", "age": 24, "email": "lakshmi24@gmail.com", "password": "pass123"},
#     {"name": "Manoj", "age": 26, "email": "manoj26@gmail.com", "password": "pass123"},
#     {"name": "Pooja", "age": 23, "email": "pooja23@gmail.com", "password": "pass123"},
#     {"name": "Ajay", "age": 27, "email": "ajay27@gmail.com", "password": "pass123"},
#     {"name": "Keerthi", "age": 22, "email": "keerthi22@gmail.com", "password": "pass123"},
#     {"name": "Naveen", "age": 25, "email": "naveen25@gmail.com", "password": "pass123"},
#     {"name": "Aishwarya", "age": 24, "email": "aishwarya24@gmail.com", "password": "pass123"},
#     {"name": "Harish", "age": 28, "email": "harish28@gmail.com", "password": "pass123"},
#     {"name": "Deepika", "age": 23, "email": "deepika23@gmail.com", "password": "pass123"}
# ]

# # collection.insert_many(users)
# # print("Data Inserted Successfully")

# # mydata = collection.find({"age":25})
# # for data in mydata:
# #     print(data)


# # Method to insert a Data in Mongo Db Compass
# # insert_one() is a PyMongo method used to insert a single document into a MongoDB collection.

# # collection.insert_one(data)
# # print("data Inserted Successfully")

# # Insert multiple documents

# # many_data = [
# #     {"name": "Bob", "department": "Engineering"},
# #     {"name": "Charlie", "department": "Marketing"}
# # ]

# # collection.insert_many(many_data)
# # print("Data Inserted Successfully")


# # Find a document
# # find_document = collection.find_one({"name": "Bob"})
# # print(find_document)



# # sort() is used to arrange the documents returned from a query in ascending or descending order based on a specified field.
# # 1 → Ascending order
# # -1 → Descending order

# # Syntax
# # collection.find().sort("field_name", order)

# # mysortedlist = collection.find().sort("age", -1)

# # for data in mysortedlist:
# #     print(data)

# # print("data Filtered successfully")



# # limit() is used to restrict the number of documents returned by a query.
# # Syntax: collection.find().limit(number)

# # data = collection.find().limit(20)
# # for d in data:
# #     print(d)

# # print(" Data Limited successfully")



# # sort() and limit() are combined to retrieve a specific number of records after sorting them.

# # Syntax: collection.find().sort("field_name", order).limit(number)

# data = collection.find().sort("age", 1).limit(5)
# for d in data:
#     print(d)

# print("Success")


# # Delete a document
# # delete_result = collection.delete_one({"name" : "Charlie"})
# # print("data deleted successfully")