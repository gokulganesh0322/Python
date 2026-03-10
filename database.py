from pymongo import MongoClient

# creating a Connection
client = MongoClient("mongodb://localhost:27017")

# Creating a database

DB = client["personal_Data"]

# Creating a Collection

collection = DB["my self"]
print("Connected Successfully")

data = {
    "name": "Gokulakrishnan",
    "course": "PYTHON FULLSTACK"
}

collection.insert_one(data)
print ("Data inserted Successfully")