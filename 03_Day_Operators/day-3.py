# Arithmetic Operations in Python
# Integers

from calendar import c


print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


# Lets practice what we have learned so far
# question 1
age = 25
# question 2
height = 1.57
# question 3
complex_number = 1+2j
# question 4
print(input("Enter your age:"))
print(input("Enter your height:"))
print(input("The area of the triangle is:"))
# question 5 - Triangle perimeter
print("Enter side a:")
a = float(input())
print("Enter side b:")
b = float(input())
print("Enter side c:")
c = float(input())

perimeter = a + b + c
print(f"Triangle perimeter: {perimeter}")

# question 6 - Rectangle area and perimeter
print("Enter the Length of a rectangle:")
length = float(input())
print("Enter the Width of a rectangle:")
width = float(input())

area = length * width
perimeter = 2 * (length + width)
print(f"Rectangle area: {area}")
print(f"Rectangle perimeter: {perimeter}")

# question 7 - Circle area and circumference
print("Enter the Radius of circle:")
r = float(input())
pi = 3.14
area = pi * r * r
circumference = 2 * pi * r
print(f"Circle area: {area}")
print(f"Circle circumference: {circumference}")

 # question 8 - Calculate slope, x-intercept and y-intercept of y = 2x - 2
print("\n=== Question 8: Line y = 2x - 2 ===")
# For y = 2x - 2:
# slope = 2
# x-intercept: when y = 0, then 0 = 2x - 2, so x = 1
# y-intercept: when x = 0, then y = 2(0) - 2 = -2

slope = 2
x_intercept = 1
y_intercept = -2

print(f"Slope: {slope}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

# question 9 - Find slope and Euclidean distance between points (2,2) and (6,10)
print("\n=== Question 9: Points (2,2) and (6,10) ===")
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate slope: m = (y2-y1)/(x2-x1)
slope = (y2 - y1) / (x2 - x1)

# Calculate Euclidean distance: sqrt((x2-x1)² + (y2-y1)²)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Slope: {slope}")
print(f"Euclidean distance: {distance}")

# question 10 - Compare the slopes in tasks 8 and 9
print("\n=== Question 10: Comparing Slopes ===")
slope_8 = 2  # from y = 2x - 2
slope_9 = 2  # from points (2,2) and (6,10)

print(f"Slope from question 8 (y = 2x - 2): {slope_8}")
print(f"Slope from question 9 (points): {slope_9}")
print(f"Are the slopes equal? {slope_8 == slope_9}")
print(f"Slope 8 > Slope 9: {slope_8 > slope_9}")
print(f"Slope 8 < Slope 9: {slope_8 < slope_9}")

# question 11 - Calculate y = x² + 6x + 9 and find when y = 0
print("\n=== Question 11: Quadratic y = x² + 6x + 9 ===")
# To find when y = 0: x² + 6x + 9 = 0
# This factors to (x + 3)² = 0, so x = -3

x_values = [-4, -3, -2, -1, 0, 1]
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
    if y == 0:
        print(f"✓ y = 0 when x = {x}")

# question 12 - Find length of 'python' and 'dragon' and make falsy comparison
print("\n=== Question 12: String Length Comparison ===")
python_len = len('python')
dragon_len = len('dragon')
print(f"Length of 'python': {python_len}")
print(f"Length of 'dragon': {dragon_len}")
print(f"Falsy comparison: {python_len == dragon_len}")  # False

# question 13 - Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
print("\n=== Question 13: 'and' operator check ===")
python_has_on = 'on' in 'python'
dragon_has_on = 'on' in 'dragon'
both_have_on = python_has_on and dragon_has_on
print(f"'on' in 'python': {python_has_on}")
print(f"'on' in 'dragon': {dragon_has_on}")
print(f"Both have 'on': {both_have_on}")

# question 14 - Use 'in' operator to check if 'jargon' is in the sentence
print("\n=== Question 14: 'in' operator check ===")
sentence = "I hope this course is not full of jargon"
has_jargon = 'jargon' in sentence
print(f"Sentence: {sentence}")
print(f"'jargon' in sentence: {has_jargon}")

# question 15 - There is no 'on' in both dragon and python
print("\n=== Question 15: No 'on' in both ===")
no_on_in_python = 'on' not in 'python'
no_on_in_dragon = 'on' not in 'dragon'
no_on_in_both = no_on_in_python and no_on_in_dragon
print(f"No 'on' in 'python': {no_on_in_python}")
print(f"No 'on' in 'dragon': {no_on_in_dragon}")
print(f"No 'on' in both: {no_on_in_both}")

# question 16 - Find length of 'python' and convert to float and string
print("\n=== Question 16: Type conversions ===")
python_length = len('python')
python_float = float(python_length)
python_string = str(python_length)
print(f"Length: {python_length} (type: {type(python_length)})")
print(f"Float: {python_float} (type: {type(python_float)})")
print(f"String: '{python_string}' (type: {type(python_string)})")

# question 17 - Check if a number is even
print("\n=== Question 17: Even number check ===")
numbers = [2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    is_even = num % 2 == 0
    print(f"{num} is even: {is_even}")

# question 18 - Check if floor division of 7 by 3 equals int(2.7)
print("\n=== Question 18: Floor division comparison ===")
floor_div = 7 // 3
int_val = int(2.7)
are_equal = floor_div == int_val
print(f"7 // 3 = {floor_div}")
print(f"int(2.7) = {int_val}")
print(f"Are they equal? {are_equal}")

# question 19 - Check if type of '10' equals type of 10
print("\n=== Question 19: Type comparison ===")
str_10 = '10'
int_10 = 10
types_equal = type(str_10) == type(int_10)
print(f"type('10') = {type(str_10)}")
print(f"type(10) = {type(int_10)}")
print(f"Types are equal: {types_equal}")

# question 20 - Check if int('9.8') equals 10
print("\n=== Question 20: int conversion check ===")
try:
    int_98 = int('9.8')
    equals_10 = int_98 == 10
    print(f"int('9.8') = {int_98}")
    print(f"Equals 10: {equals_10}")
except ValueError as e:
    print(f"Error: {e}")
    print("Cannot convert '9.8' to int directly")

# question 21 - Calculate weekly pay
print("\n=== Question 21: Weekly Pay Calculator ===")
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print(f"Your weekly earning is {pay}")

# question 22 - Calculate seconds lived
print("\n=== Question 22: Lifetime in Seconds ===")
years = int(input("Enter number of years you have lived: "))
seconds_per_year = 365 * 24 * 60 * 60  # 365 days * 24 hours * 60 minutes * 60 seconds
total_seconds = years * seconds_per_year
print(f"You have lived for {total_seconds} seconds.")

# question 23 - Display the table
print("\n=== Question 23: Number Table ===")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
