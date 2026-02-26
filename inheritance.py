# # Python supports five main types of inheritance

# # 1. Single Inheritance - One subclass inherits from one superclass.
# # A child class inherits from one parent class.

# class Vehicle():
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed

#     def dispplay_info(self):
#         return f"My Vehicle is {self.brand} and {self.speed} speed"


# class Car(Vehicle):
#     pass


# object_one = Car("Audi","150 KMP")
# print(object_one.brand)


# # 2. Multiple Inheritance
# # A child class inherits from more than one parent class.

# class Father:
#     def skill1(self):
#         print("Gardening")

# class Mother:
#     def skill2(self):
#         print("Cooking")

# class Child(Father, Mother):
#     pass

# john = Child()
# john.skill1()
# john.skill2()



# # # 3. Multilevel Inheritance
# # # A class inherits from a class that already inherits from another class.


# class third():
#     def greet(self):
#         print("Hello world")

# class Second(third):
#     pass

# class First(Second):
#     pass

# john = First()
# john.greet()





# # 4. Hierarchical Inheritance
# # Multiple child classes inherit from the same parent class.

# class Parent:
#     def property(self):
#         print("Shared property")

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# class Child3(Parent):
#     pass


# object_one = Child1()
# object_two = Child2()
# object_three = Child3()


# object_one.property()
# object_two.property()
# object_three.property()



# # 5. Hybrid Inheritance

# # A combination of two or more types of inheritance.