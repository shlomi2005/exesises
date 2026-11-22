# excercise 1

first_name = "David"
last_name = "Cohen"
age = 25
city = "Tel Aviv"
email = "david@gmail.com"

print(f"""
===== User Details =====
First Name: {first_name}
Last Name: Cohen {last_name}
Age: {age}
City: {city}
Email: {email}
========================
""")


# excercise 2
birth_year = 2005
current_year = 2026
age = current_year - birth_year
print(f"You are approximately {age} years old.")

# excercise 3
width = 4
height = 2
Area = width * height
Scope = width * 2 + height * 2
print(f"area = {Area}")
print(f"Scope = {Scope}")

# excercise 4
name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(salary))

# excercise 5
name = input("enter a first name: ")
last_name = input("enter a last name: ")
city = input("enter a your city: ")
age = int(input("enter a your age: "))
print(
    f"welcomme {name} {last_name} You live in {city} And you are {age} years old")

# excercise 6
num_1 = int(input("enter a number 1: "))
num_2 = int(input("enter a number 2: "))
print(f"""
{num_1+num_2}
{num_1-num_2}
{num_1*num_2}
{num_1/num_2}
""")
# excercise 7
name = input("enter a name for product: ")
price = int(input("enter a price for product: "))
amount = int(input("enter amount for products: "))
all_price = amount * price
print(f"""
====== Purchase Receipt ======
Product: {name}
Price: {price}
Quantity: {amount}
Total: {all_price}
==============================
""")

# excercise 9
name = input("Enter the employee's name: ")
number_of_working = int(input("Number of working hours per month: "))
hourly = int(input("enter a hourly rate: "))
total_for_month = number_of_working * hourly
print(f"""
==============================
name  {name}
number_of_working {number_of_working}
hourly {hourly}
total_for_month = {total_for_month}
==============================
""")


# excercise 10
bill_amount = float(input("enter a total price for bill: "))
percentage_tip = float(input("enter a percentage_tip: "))
number_diners = int(input("enter a number_diners: "))
tip_amount = bill_amount*percentage_tip/100
total_price = bill_amount+tip_amount
total_per_diner = total_price/number_diners
print(f"""
==============================
tip_amount = {tip_amount}
total_price = {total_price}
total_per_diner = {total_per_diner}
==============================
""")


# excercise 12
a = 10
b = 20
c = a
a = b
b = c
print(f"""
a = {a}
b = {b}
""")


name = input("enter a first name: ")
last_name = input("enter a lest name: ")
age = int(input("enter a your age: "))
name_scoole = input("rnter a name scoole: ")
name_course = input("enter a name_course: ")
number_months_study = int(input("enter a number of months of study: "))
price_month = int(input("enter a price_month: "))
total_price_1 = price_month * number_months_study
print(f"""
================================
       STUDENT REGISTRATION
================================

Student: {name} {last_name}
Age: {age}
Institution: {name_scoole}
Course: {name_course}
Duration: {number_months_study}
Monthly Price: {price_month}

Total Course Price: {total_price_1}

================================
Registration completed!
================================
""")
