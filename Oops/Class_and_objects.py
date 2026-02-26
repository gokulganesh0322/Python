# # Object-Oriented Programming (OOP) in Python is a programming paradigm that organizes code 
# around objects, which are instances of classes. It focuses on bundling related data (attributes)
#  and behaviors (methods) into a single, self-contained unit to create modular, reusable, 
# and maintainable applications



# # A class is a blueprint or template used to create objects.
# # It defines variables (data) and functions (methods) that the objects will have.


# # An object is an instance of a class.
# # It represents a real-world entity and can access the data and methods defined in the class.

# # Class
# class Car():

#     # Attibutes (Varibles)
#     colour = "White"
#     speed = 200
#     milage = 15

#     # Methods(Functions)
#     def brake(self):
#         print("The Car has stopped running")



# # Object   
# Audi = Car()


# Audi.colour = "Red"
# print(Audi.colour)

# Audi.speed = 250
# print(Audi.speed)

# Audi.milage = 20
# print(Audi.milage)


# Audi.brake()



# A constructor in Python is a special method used to initialize (assign values to) the object’s data when an object is created.

# __init__()


# class Animal:

#     def  __init__(self, colour , legs , sound):
#         self.colour = colour
#         self.legs = legs
#         self.sound = sound
    





# Cow = Animal("Black", 4 , "Cowsound")
# Dog = Animal("Brown", 4 , "Barking" )
# print(Cow.colour)
# print(Dog.sound)


# 1. Constructor (__init__)

# * Takes three parameters: make (string), model (string), and year (integer).
# * Initializes these as attributes of the class.

# class bike():
#      def __init__(self,make,model,year):
#           self.make=make
#           self.model=model
#           self.year=year


# Bike=bike("Pulser","Classic",2020)
# print(Bike.make)
# print(Bike.model)
# print(Bike.year)
          


# # 2. Methods:

# # * display_info(self) → Prints all the car’s details as: "Car: <year> <make> <model>"
# # * age(self, current_year) → Returns the age of the car: current_year - year



# class car():
#     def __init__(self,year,make,model):
#         self.year=year
#         self.make=make
#         self.model=model

#     def age(self,currentyear):
#             return currentyear - self.year

# car_1=car(2022,"TATA","ALTO 800")
# print(car_1.make)

# print("car age: ",car_1.age(2025))




