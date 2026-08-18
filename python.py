from os import replace


print("My learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI")

#Dynamic variables
info_mail = "infotext@gmail.com"
support_mail = "support@gmail.com"
website = "dataworld.com"

print(f"""
      Welcome to {website} where learning is fun. Incase you need more information
      kindly email the request to {info_mail} and incase of support with our programs
      email: {support_mail}""")

# user inputs to a program

name = input("Enter your name:: ")

print(f"My name is::{name}")

# python data types
#single value
int  = 20
float = 4.2
str = 'yeh'
bool = False
h = None # no value or nothing - used ot show absence on any data
i = "" # is a string with no characters inside not a None
o = " " # is a string with white space
#multi-values
list = [[1],[2],[3]]
set = {[2],[5]}
tuple = ([6],[8])
dict =  {['u':4],['d':7]}

a = 29


# data types, functions and methods
# functions types

# standalone functions like 
print()

# methods of class such as 
replace()

# operations - magic methods
+ - == < >


#user defined functions

defined by user for a specific case

# 3rd party functions
such as tensorflow

# standard built-in module: 

# functions: independent block of code function_name(value)
#  methods: functions belong to objects/classes value.method_name()

text = "hi"
number = 10

print(text)
print(number)

print(type(text))
print(type(number))

print(len(text))
print(len(number))

text.upper()
number.bit_length()

#challenge

age = 94
height = 75
name = "Jay"
are_you_a_student = False
student_debt = None

#print values
print(age)
print(height)
print(name)
print(are_you_a_student)
print(student_debt)

#data types
print(type(age))
print(type(height))
print(type(name))
print(type(are_you_a_student))
print(type(student_debt))

#length
print(len(age))
print(len(height))
print(len(name))
print(len(are_you_a_student))
print(len(student_debt))