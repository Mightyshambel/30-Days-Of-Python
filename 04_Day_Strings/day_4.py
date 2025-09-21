
# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip()) # 'thirty days of python'

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String
  
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

# 💻 Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
newCourse= " ".join(['Thirty', 'Days', 'Of', 'Python'])
print(newCourse)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

coding = "" .join(['Coding', 'For' , 'All'])
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
variable="Coding For All"

# 4. Print the variable company using print().
print(variable)

# 5. Print the length of the company string using len() method and print().

print(len("company"))
# 6. Change all the characters to uppercase letters using upper() method.
# Your code here
newCompany = "company"
print(newCompany.upper())
# 7. Change all the characters to lowercase letters using lower() method.
# Your code here
print(newCompany.lower())
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# Your code here
print(newCompany.capitalize())
print(newCompany.title())
print(newCompany.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
# Your code here
newCoding="coding"
print(newCoding.strip("cg"))
# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
# Your code here
print(coding.index("Coding"))
# 11. Replace the word coding in the string 'Coding For All' to Python.
# Your code here
print(coding.replace("coding","Python"))
# 12. Change Python for Everyone to Python for All using the replace method or other methods.
# Your code here
py = "Python for Everyone"
print(py.replace("Everyone","All"))

# 13. Split the string 'Coding For All' using space as the separator (split()).
# Your code here
print(variable.split())
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# Your code here
faang="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(faang.split(","))
# 15. What is the character at index 0 in the string Coding For All.
# Your code here
print(variable[0])
# 16. What is the last index of the string Coding For All.
# Your code here 
print(variable[-1])

# 17. What character is at index 10 in "Coding For All" string.
# Your code here
print(variable[10])
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Your code here
py = "Python for Everyone"
print("".join(w[0] for w in py.split()))
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
# Your code here
print("".join(word[0] for word in variable.split()))
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# Your code here

print(variable.index("C"))
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# Your code here
print(variable.index("F"))
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Your code here
ppl ="Coding For All People."
print(ppl.rfind("l"))
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Your code here
sentence = 'You cannot end a sentence with because because because is a conjunction'
print("This is the place of becuase ",sentence.find("because"))
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Your code here
print("This is the place of becuase with rindex",sentence.rindex("because"))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Your code here
print(sentence.replace("because because because",""))

# 26. Find the position of the first occurrence of the word 'because' in the following sentence:
print(sentence.find("because"))

# 27. Slice out the phrase 'because because because' in the following sentence:

print(sentence.replace("because because because",""))
# 28. Does 'Coding For All' start with a substring 'Coding'?

print(variable.startswith("Coding"))
# 29. Does 'Coding For All' end with a substring 'coding'?

print(variable.endswith("coding"))

# 30. '   Coding For All     ', remove the left and right trailing spaces in the given string.dirty_string = '   Coding For All     '
dirty_string = '   Coding For All     '
print(dirty_string.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():

print(variable.isidentifier())
not_var = "30daysofpythonmighty"
print(not_var.isidentifier())
# 32. The following list contains the names of some python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries =['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(libraries))
# 33. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")
# 34. Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
# 35. Use the string formatting method to display the following:
"""sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""
radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radious {radius} is 314 meters sqaure:")
# 36. Make the following using string formatting methods:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
a=8
b=6
print(f" {a} + {b} = {a+b}")
print(f" {a} - {b} = {a-b}")
print(f" {a} * {b} = {a*b}")
print(f" {a} / {b} = {a/b}")
print(f" {a} % {b} = {a%b}")
print(f" {a} // {b} = {a//b}")
print(f" {a} ** {b} = {a**b}")
