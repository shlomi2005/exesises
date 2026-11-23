# # excercise 1
# age = int(input("enter yuor age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")


# # excercise 2
# num = int(input("enter yuor number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# if num == 0:
#     print("Zero")


# # excercise 3
# num = int(input("enter yuor number: "))
# if num % 2 == 0:
#     print("double")
# else:
#     print("odd number")

# # excercise 4
# num1 = int(input("enter yuor number: "))
# num2 = int(input("enter yuor number: "))
# if num1 == num2:
#     print("The numbers are equal.")
# elif num1 > num2:
#     print(num1)
# else:
#     print(num2)


# # excercise 5
# password = input("enter your password: ")
# if password == "Python123":
#     print("Access Granted")
# else:
#     print("Access Denied.")


# # excercise 6
# num = int(input("enter yuor number: "))
# if num < 100 and num > 50:
#     print("בין 51 ל-100.")
# elif num < 50 and num > 10:
#     print("בין 11 ל-50.")
# elif num < 10 and num > 0:
#     print("בין 1 ל-10.")
# else:
#     print("מחוץ לתווך")


# # excercise 7
# score = int(input("enter your score: "))
# if score > 100:
#     print(False)
# elif score >= 90:
#     print("Excellent")
# elif score >= 80:
#     print("Very Good")
# elif score >= 70:
#     print("Good")
# elif score >= 60:
#     print("Passed")
# else:
#     print("Failed")


# # excercise 8
# correct_username = "admin"
# correct_password = "123456"

# name = input("enter user name: ")
# password = input("enter your password: ")
# if name == correct_username and password == correct_password:
#     print("Login Successful")
# elif name == correct_username and password != correct_password:
#     print("Wrong Password")
# else:
#     print("Unknown User")


# # excercise 9
# age = int(input("enter age: "))
# price = int(input("enter price the product: "))
# if age >= 60:
#     price = price * 0.80
# elif age < 18:
#     price = price * 0.90
# else:
#     price = price
# print(price)


# # excercise 10
# num = int(input("enter yuor number: "))
# if num % 3 != 0 and num % 5 != 0:
#     print("number not divisible 3 and 5")
# elif num % 3 == 0 and num % 5 == 0:
#     print("number divisible 3 and 5")
# elif num % 3 == 0:
#     print("number divisible 3")
# elif num % 5 == 0:
#     print("number divisible 5")


# # excercise 11
# age = int(input("entar your age: "))
# if age >= 18:
#     print("May enter")
# elif age >= 16:

#     adult_accompaniment = bool(int(input(
#         "Did you arrive accompanied by an adult? To confirm, press 1; to cancel, press 0.")))
#     if adult_accompaniment:
#         print("May enter")
#     else:
#         print("not May enter")
# else:
#     print("not May enter")


# # excercise 12
# average = float(input("enter your average the greades: "))
# monthly_income = float(input("enter your monthly income: "))
# if average > 90:
#     print("Eligible for a scholarship.")
# elif average > 85 and monthly_income < 5000:
#     print("Eligible for a scholarship.")
# else:
#     print("Not eligible for a scholarship.")


# # excercise 13
# correct_username = "admin"
# correct_password = "123456"
# name = input("enter user name: ")
# password = input("enter your passwored: ")
# is_acount_active = bool(
#     int(input("Is the account active? For active, press 1; for inactive, press 0.")))

# if name == correct_username and password == correct_password and is_acount_active:
#     print("Entry has been approved.")
# else:
#     print("Entry was not approved.")


# # excercise 14
# num = int(input("enter yuor number: "))
# if num >= 20 and num <= 80:
#     print("The Number in the Middle")
# else:
#     print("The Number not in the Middle")


# num = int(input("enter yuor number: "))
# if not (num < 20) and not (num > 80):
#     print("The Number in the Middle")
# else:
#     print("The Number not in the Middle")


# # excercise 15
# balance = 5000
# withdrawal_amount = int(input("Enter the withdrawal amount: "))
# if withdrawal_amount > 0:
#     if withdrawal_amount <= balance:
#         print(
#             f"The withdrawal was successful. Remaining in your account {balance-withdrawal_amount}:")
#     elif withdrawal_amount > balance:
#         print(f"{withdrawal_amount} Greater than {balance} ")
# else:
#     print(f"number must be positive number")

# # excercise 16
# age = int(input("enter your age :"))
# club_member = bool(
#     int(input("Are you a club member? To confirm, press 1; to cancel, press 0: ")))
# if age < 12:
#     total_price = 25
# elif age < 18:
#     total_price = 35
# elif age >= 18:
#     total_price = 50
# if club_member:
#     total_price = total_price * 0.90
# print(total_price)


# # excercise 17
# age = int(input("enter your age: "))
# monthly_income = int(input("enter the monthly income: "))
# Seniority = bool(int(input(
#     "How many years of seniority do you have? If more than one year, press 1; otherwise, press 0: ")))
# if age > 21 and monthly_income >= 7000 and Seniority:
#     print("The loan has been approved.")
# elif age > 21 and monthly_income >= 7000 and not Seniority:
#     print("The loan was not approved; you must have more than one year of seniority.")
# elif age > 21 and monthly_income < 7000 and Seniority:
#     print("The loan was not approved; you must have an income of over 7,000 per month.")
# elif age < 21 and monthly_income >= 7000 and Seniority:
#     print("The loan was not approved; you must be 21 years of age or older.")

# # excercise 18
# vehicle_type = int(input(
#     "Enter the vehicle type: for a motorcycle, press 1; for a private car, press 2; for a commercial vehicle, press 3: "))
# many_hours = int(input(
#     "How many hours will you be in the parking lot? For less than an hour: "))
# if vehicle_type == 1:
#     if many_hours == 1:
#         print(10 * 0.90)
#     elif many_hours < 5:
#         print(10*many_hours)
#     elif many_hours >= 5:
#         print(10*many_hours*0.90)
# elif vehicle_type == 2:
#     if many_hours == 1:
#         print(20 * 0.90)
#     elif many_hours < 5:
#         print(20*many_hours)
#     elif many_hours >= 5:
#         print(20*many_hours*0.90)
# elif vehicle_type == 3:
#     if many_hours == 1:
#         print(30 * 0.90)
#     elif many_hours < 5:
#         print(30*many_hours)
#     elif many_hours >= 5:
#         print(30*many_hours*0.90)


# # excercise 19
# num1 = int(input("enter a number1: "))
# num2 = int(input("enter a number2: "))
# total = 0
# desired = input("Enter the desired action: (+ - / *)")
# if desired not in ["*", "/", "+", "+"]:
#     print("The action does not exist")
# if desired == "+":
#     print(num1 + num2)
# elif desired == "/":
#     if num2 == 0:
#         print("It is not possible to divide by 0.")
#     else:
#         print(num1/num2)
# elif desired == "*":
#     print(num1*num2)
# elif desired == "-":
#     print(num1 - num2)


# # excercise 20
# year = int(input("enter year: "))
# if year % 400 == 0:
#     print("leap year")
# elif year % 100 == 0 and year % 400 != 0:
#     print("leap not year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("leap year")
# else:
#     print("leap not year")

# # excercise 21
# hours = float(input("Enter the number of working hours: "))

# if hours <= 182:
#     salary = hours * 50
# elif hours <= 184:
#     salary = 182 * 50 + (hours - 182) * 50 * 1.25
# else:
#     salary = 182 * 50 + 2 * 50 * 1.25 + (hours - 184) * 50 * 1.5

# print("Total salary:", salary)


# # excercise 22
# age = int(input("Enter customer age: "))
# amount = float(input("Enter purchase amount: "))
# is_member = input("Is the customer a club member? (yes/no): ") == "yes"
# is_opened = input("Was the product opened? (yes/no): ") == "yes"
# has_invoice = input("Is there a purchase invoice? (yes/no): ") == "yes"
# days = int(input("Enter the number of days since purchase: "))

# if not has_invoice:
#     print("Not eligible for a refund")
#     print("Reason: no purchase invoice")
# elif is_opened:
#     print("Not eligible for a refund")
#     print("Reason: the product was opened")
# elif amount <= 0:
#     print("Not eligible for a refund")
#     print("Reason: the purchase amount must be greater than zero")
# else:
#     if (is_member and days <= 30) or (not is_member and days <= 14):
#         print("Eligible for a refund")
#         print("Refund amount:", amount)
#     else:
#         print("Not eligible for a refund")
#         if is_member:
#             print("Reason: more than 30 days have passed since the purchase")
#         else:
#             print("Reason: more than 14 days have passed since the purchase")
