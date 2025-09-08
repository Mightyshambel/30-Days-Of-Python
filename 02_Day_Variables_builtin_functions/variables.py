
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


#Lets Practice variable naming side by side with the instructor using snake_name naming convention

first_name="Mighty"
last_name="Shambel"
citizenship="Ethiopian"
age=25
role="Full Stack Developer"
gender="Girl"
student=True
 #printing out the values

#This is python baby gurl indentation matters be careful:)
#Also when concatenating dont use + comma is enough

print("In amharic we call it erzmet but now the length of my name is",len(first_name))
print("First Name",first_name)
print("Last name",last_name)
print("My Citizenship is",citizenship)
print("Born in 2000 which means am",age)
print("Aspiring data scientist but at the moment i am ",role)
print("yes i like pink and i am a ",gender)
print("yes i am a student thats ",student)

#another thing we can do is multiple  variable declaration
skills , location, weight, fav_artist = "HTML,CSS,JAVASCRIPT,ANGULAR,PYTHON", "Venice",52,"Riri"

print(skills , location, weight, fav_artist)
print ("This are the programming languges i have been working ", skills ,"Hit me up when you are in",  location, "am so tiny yes am --kgs", weight,"Who is  your favourite artist ?", fav_artist ,"yes thats my gurl")