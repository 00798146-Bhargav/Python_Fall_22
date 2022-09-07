# Program#2
# Bhargav Reddy Lankireddy
# Id: 00798146
# String Methods
#Version Control : https://github.com/00798146-Bhargav/Python_Fall_22/tree/Week2_Program%232


stringA = "Hello"
stringB = "World"

# String Method - Capatalize

"""
The first character if the string is converted to upper case
and the rest are converted to lower case
"""
print(f"Capatalize Method for stringA {stringA.capitalize()}")

print(f"Capatalize Method for stringB {stringB.capitalize()}")

# String Method - casefold()

"""
The casefold() method returns a string where all the characters are lower case
it's more Aggresive compared to lower() method
Equality condition is more Accurate

"""


print(f"Casefold Method for stringA {stringA.casefold()}")

print(f"casefold Method for stringB {stringB.casefold()}")


# String Method - center()

"""
Returns a string padded with specified fillchar and it doesn't modify the original string
"""
print(f"Center Method for stringA {stringA.center(20,'A')}")

print(f"Center Method for stringB {stringB.center(20,'B')}")

# String Method - count()

"""
Returns a integer Value , no of times input value appears in the string
"""

print(f"Count method for stringA counting Occurence of 'e' {stringA.count('e')}")
print(f"Count method for stringB counting Occurence of 'd' {stringB.count('d')}")

# String Method - endsWith()

"""
Returns a Boolean Value , if input ends with specified characters
"""

print(f"endsWith method for stringA ends with 'o' {stringA.endswith('o')}")
print(f"endsWith method for stringB ends with 'a' {stringB.endswith('a')}")


# String Method - find()

"""
Returns a integer Value , check for first occurence 
if value is founf return index 
else return -1
"""

print(f"find method for stringA - Hello find  'o' {stringA.find('o')}")
print(f"find method for stringB - World find  'r' {stringB.find('r')}")


# String Method - format()

"""
format the given string as a user defined
"""

text = "pyhton class happening on {day} and timings is {time}".format(day="Tuesday" , time="6:30")
print(text)


# String Method - index()

"""
returns index value if value is found, not raises a Exception
"""

print(f"index method for stringA - Hello index  'o' {stringA.index('o')}")
print(f"index method for stringB - World index  'r' {stringB.index('r')}")

# String Method - replace()

"""
modifies a input string if match is found 
"""

text1 = "Python"
result = text1.replace('n','i')

print(f"replace method for stringA - Hello replace index  'o' {result}")


# String Method - split()

"""
converts input value into list 
"""
splitString = "I Love Python"

resultSplitString = splitString.split(" ")

print(f"split given string into list {resultSplitString}")

# String Method - startswith()

"""
return Boolean value, if it starts  with specified string
"""

print(f"startWith method for stringA start with 'H' {stringA.startswith('H')}")
print(f"startWith method for stringB start with 'D' {stringB.startswith('d')}")


# String Method - strip()

"""
remove whitespaces from Beginings and end of the String  
"""
stripString = "   Python   "

print(f"strip method for removing whitespaces {stripString.strip()}")


# String Method - upper()

"""
converts string into upper case
"""

print(f"upper method for StringA - Hello {stringA.upper()}")


# String Method - title()

"""
converts first character string into upper case
"""

titleString = "python"

print(f"title method for titleString - python {titleString.title()}")


# String Method - join()

"""
The join() method takes all items in an iterable and joins them into one string.
"""

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(f" join method {x}")



# String Method - rsplit()

"""
method splits a string into a list, starting from the right.
"""

rsplitString = "apple, banana, cherry"

x = rsplitString.rsplit(", ")

print(f" rsplit method {x}")























