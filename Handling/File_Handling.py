# File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.


# Syntax
# file = open('filename.txt', 'mode')


# Creating a File
# file = open('myfile.txt', "x")
# print("File Created")


# Writing in a File
# wrirtefile = open("myfile.txt", "w")
# wrirtefile.write("Hello Gokul * 2 , Bose")
# print("Written Successfully")


# Creating File with Write Mode
# writecreate = open("new.txt", "w")
# writecreate.write("I am a New file created with write Mode")
# print("Written and created Successfully")



# edit = open("new.txt", "w")
# edit.write("I am Overwrote it")
# print("Over Wrote Completed")

# edit = open("new.txt", "w")
# edit.write("   I am adding at the end   ")
# print("Append completed")