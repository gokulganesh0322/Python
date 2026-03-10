# Polymorphism in Python refers to the ability of different objects to respond
#  to the same method or function call in ways specific to their individual types.


# Method overloading is a feature where multiple methods in the same 
# class have the same name but different parameters


# class Maths():
#     def add(self, *args):
#         return sum(args)


# obj = Maths()

# print(obj.add(6))
# print(obj.add(8,7,6,5))


# Method overriding in Python is an object-oriented programming concept 
# that allows a child class (subclass) to provide a specific implementation
#  for a method that is already defined in its parent class (superclass). 


# class Animal():
#     def sound(self):
#         return(" I make Animal Sound")

# class Cow(Animal):
#     def sound(self):
#         return(" I make Cow sound ")

# class Dog(Animal):
#     def sound(self):
#         return "I make Dog Sound"


# obj1 = Animal()
# obj2 = Cow()
# obj3 = Dog()

# # obj1.sound()
# # obj2.sound()
# # obj3.sound()


# demo = [Animal(), Cow(), Dog()]
# for x in demo:
#     print(x.sound())



# TASK

# Create a class called Shape with a method area().
# Then create two subclasses Rectangle and Circle that override the area() method.
# Write a loop that stores different shape objects in a list and prints
# their areas using polymorphism.


# class Shape():
#     def area(Self):
#         return("Total Space of Area")
    
# class Rectangle(Shape):
#     def area(self):
#         return("Total Rectangle of Area")
    
# class Circle(Shape):
#     def area(self):
#         return("Total Circle of Area")
    
# obj1 = Shape()
# obj2 = Rectangle()
# obj3 = Circle()

# Overall = [Shape(),Rectangle(),Circle()]

# for x in Overall:
#     print(x.area())





# Implement method overloading in a class Calculator using *args:
# If 2 numbers are passed, return their multiplication.
# If 3 numbers are passed, return their average.
# If more than 3 numbers are passed, return their sum.



class Calculator():
    def calculate(self, *args):
        if len(args) == 2:
            return args[0] * args[1]

        elif len(args) == 3:
            return sum(args) / 3

        elif len(args) > 3:
            return sum(args)

        else:
            return "Please pass at least two numbers"
        

Object = Calculator()

print(f"VAlue :",Object.calculate(5,5,6,5,89,6))