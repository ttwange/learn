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

# working with strings
password = input("enter password: ")

if len(password) < 8:
    print("Ensure atleast password is atleast 8 character")
else:
    print(password)

paragraph = """
Python is easy to learn.
Python is powerful.
Many people love Python
"""

print(paragraph.count("Python"))


# generate
phone = "174-3857-09"

print(phone.replace("-",""))

phone_b = []
for i in phone:
    if  i == '-':
        continue
    else:
        phone_b.append(i)
        
phone = "174385709"

reversed_phone = ""
for char in phone:
    reversed_phone = char + reversed_phone

print(reversed_phone)

## python

word = "object has no attribute"

print(word[:-1])
print(word[-1:])
len(word)

print(word.find("no"))

last_name = "Doe"
school = "Masinde Muliro University of Science and Technology"

print(last_name)
print(school)

score = -45
print(score)

#basic maath operations
#addition
total = 10 + 5
print(total)
change =  10 -  5
print(change)

#multiplication and division
area =  6 * 4
print(area)
quarter = 6 / 4
print(quarter)

# power 
squared = 6 ** 2
print(squared)

#integer and float division
float_result = 10/ 3
print(float_result)
round_result = 10 // 3
print(round_result)

# strings
country = "Mongolia"
city = 'Cape Verde'

reason = """Random country and city that came first inside thy brain"""

print(country)
print(city)
print(reason)

# converting to string

cost = 1500000
mileage = 24000

message = f"the price of an imported AT with {mileage} km to Kenya is ksh {cost}"

print(message)


#booleans

profit = 200

print(profit > 110)
print(profit < 90)
print(profit >= 1000)
print(profit <= 290)



print(message.title())  

# control flow

if mileage < 15000 and cost < 1600000:
    print("Greate deal")
else:
    print("Continue with the search")
    
def check_user(user):
    if user is not None:
        if user.get("active"):
            return "OK"
    return "Invalid"

ek = "ek99"
status = "employee" if ek == "ek99" else "not an employee"
status

statement = "We just posted a new course from Andrew Brown on the"

for index, i in enumerate(statement):
    if i =='p':
        print(index, i)
        continue
    elif i == 'e':
        print(index,i)
        continue
    

for num in range(10):
    if num == 5:
        break
    if num % 2 == 0:
        continue     # skip rest of this iteration, go to next num
    print(num)       # only odd numbers less than 5: 1, 3
    
    
for i in range(5):
    if i == 3:
        continue
    print(i)
    
it will print 0,1,2,3,4 for range(5)
it will only print i if its not equal to 3. where if we get 3 it will move to the next iter and print the number as long as its not 3.

fruits = ["apple", "banana"]

fruits.append("cherry")     # add to end -> O(1)
fruits.insert(0, "mango")   # add at position -> O(n), shifts everything right
fruits.remove("mango")     # remove by value -> O(n), searches first
popped = fruits.pop()       # remove & return last item -> O(1)
print(fruits[1:3])          # slicing -> new list, doesn't mutate original


words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1   # get returns 0 if not seen yet

print(counts)   # {"apple": 3, "banana": 2, "cherry": 1}


point = (36.8219, -1.2921)

print(point[0])        # 36.8219 -> indexing works, same as lists
print(point[-1])       # -1.2921 -> negative indexing works too
lat, lon = point        # unpacking — very common in real code

point[0] = 10        # TypeError: 'tuple' object does not support item assignment
point.append(5)      # AttributeError: 'tuple' object has no attribute 'append'

#functions

def events(event):
    print(f"Tomorrow's event is {event}")
    
events("Olympics")

def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
add_item(["ke","tz"])
add_item(["ug"])