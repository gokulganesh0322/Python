


from pymongo import MongoClient

# creating a Connection
student = MongoClient("mongodb://localhost:27017")

# Creating a database

DB = student["student_data"]

# Creating a Collection

collection = DB["my self"]
print("Connected Successfully")

std1 = {
    "name": "G.Gokulakrishnan",
    "course": "M.com",
    "Reg No": "41330722009"
}


std2 = {
    "name": "Dinesh Kumar",
    "course": "M.com",
    "Reg No": "41330722010"
}

std3 = {
    "name": "Roopak Roshan",
    "course": "M.com",
    "Reg No": "41330722011"
}

std4 = {
    "name": "Ilango",
    "course": "M.com",
    "Reg No": "41330722012"
}

std5 = {
    "name": "Sundara Moorthy",
    "course": "M.com",
    "Reg No": "41330722013"
}

std6 = {
    "name": "Mani",
    "course": "M.com",
    "Reg No": "41330722014"
}

std7 = {
    "name": "Siva Shankaran",
    "course": "M.com",
    "Reg No": "41330722015"
}

std8 = {
    "name": "Vicky",
    "course": "M.com",
    "Reg No": "41330722016"
}

std9 = {
    "name": "Raj Kumar",
    "course": "M.com",
    "Reg No": "41330722017"
}

std10 = {
    "name": "Velu",
    "course": "M.com",
    "Reg No": "41330722018"
}



collection.insert_one(std1)
collection.insert_one(std2)
collection.insert_one(std3)
collection.insert_one(std4)
collection.insert_one(std5)
collection.insert_one(std6)
collection.insert_one(std7)
collection.insert_one(std8)
collection.insert_one(std9)
collection.insert_one(std10)
print ("Data inserted Successfully")