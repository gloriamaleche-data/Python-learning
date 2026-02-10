# A simple report card printer for one student.
""" Brings in practice the use of variables, assignment, data types,
printing, and booleans.
The first core principles of python"""

name = 'Alice' #Variable assignment of a string value denoted by either single or double quotes
print(name) #The print() function is responsible for generating output back to the terminal
print(type(name))# The type() function denotes the data type of a variable, and while nestled within print(), generates the output to the monitor
print(name, type(name)) # Cncatinating the two print statements

is_student = True #A boolean data type denotes a yes or no condition, no in between. Represented by True or False
print(is_student, type(is_student)) #Print() function can display more than one value at a time separated by a comma

age = 20 #Assigning an integer data type to our variable age
print(age, type(age))

score = 80.5 #Assigning a float data type
print(isinstance(score, int)) #Output is false. isinstance() function checks whether score is of the data type 'int'. Returns a boolean value.
print(isinstance(score, float)) #Output is true
print(score. type(score))

"""This practice also includes the practical steps on how to import a project from Python to GitHub using the commandline or Git"""