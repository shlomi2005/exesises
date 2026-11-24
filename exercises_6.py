# # excercise 1

# numbers = (10, 20, 30, 40, 50)
# print(numbers)
# print(numbers[0], numbers[-1])
# print(len(numbers))
# print(numbers[2])


# # excercise 2
# users = ("Moshe", "David", "Dana", "Noa", "Michael")
# for user in users:
#     print(user)
# if "Moshe":
#     print(True)
#     print(len(users))


# # excercise 3
# numbers = (10, 20, 30, 40, 50, 32, 4, 5, 43, 54, 5, 66)
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[::-1])


# # excercise 4
# product = ("pen", 150, 3, "pro")


# # excercise 5
# print(product[0])
# print(product[1])
# print(product[2])
# print(product[3])

# # excercise 6
# count = 0
# big = 0
# double = 0
# numbers = (10, 20, 30, 40, 50, 32, 4, 5, 43, 54, 5, 66)
# for num in numbers:
#     count += num
#     if num > big:
#         big = num
#     if num % 2 == 0:
#         double += 1

# print(f"count = {count}")
# print(f"big = {big}")
# print(f"double = {double}")


# # excercise 7
# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
# new = products[:3]
# new1 = products[-2:]
# new2 = new+new1
# print(new)
# print(new1)
# print(new2)


# # excercise 7
# student = {"name": "David", "age": 22, "grade": 95, "city": "haifa"}
# print(student["name"])
# print(student["age"])
# print(student["grade"])
# print(student["city"])


# # excercise 8
# car = {"brand": "Toyota", "model": 5, "year": 1985, "price": 22000}
# car["price"] = 23000
# car["year"] = 1995
# car["color"] = "yeloo"
# print(car)


# # excercise 9
# salaries = {"David": 12000,    "Moshe": 15000,    "Dana": 13500}
# print(salaries["David"])
# print(salaries["Moshe"])
# print(salaries["Dana"])
# salaries["Dana"] = 10000
# salaries["Yakov"] = 17000
# print(salaries)


# # excercise 10
# products = {"Milk": 7, "Sliced Bread": 9, "Eggs": 14, "Yellow Cheese": 22, "Cucumbers": 6,
#             "Tomatoes": 8, "Chicken Breast": 35, "White Rice": 10, "Olive Oil": 40, "Instant Coffee": 27}
# product_for_user = input("enter a name for product: ")

# if product_for_user in products:
#     print(products[product_for_user])
# else:
#     print("the product not in store.")


# # excercise 11
# grades = {"Noa": 95, "Daniel": 88, "Maya": 92, "Itay": 79, "Yael": 100}
# for k, v in grades.items():
#     print(f"Student {k} | Grade {v}")


# # excercise 12
# count = 0
# big = 0
# hige = ""
# loose = 0
# grades = {"David": 90,    "Moshe": 75,
#           "Dana": 100,    "Noa": 55,    "Avi": 82}
# leni = len(grades)
# for k, v in grades.items():
#     count += v
#     if v > big:
#         big = v
#         hige = k
#     if v > 80:
#         print(k)
#     if v < 60:
#         loose += 1

# print(count/leni)
# print(hige)
# print(loose)


# # excercise 13
# products = {"Milk": 7, "Sliced Bread": 9, "Eggs": 14, "Yellow Cheese": 22, "Cucumbers": 6,
#             "Tomatoes": 8, "Chicken Breast": 35, "White Rice": 10, "Olive Oil": 40, "Instant Coffee": 27}
# product_for_user = input("enter a name for product: ")
# if product_for_user in products:
#     print("the product true")
#     new_user = int(
#         input("Do you want to update the price? Press 1 to confirm, or press 2 to exit."))
#     if new_user == 1:
#         products[product_for_user] = int(input("enter new price: "))
#     else:
#         print("good_by")
# else:
#     new_product = int(input(
#         "The product is not in the list. Would you like to add it? Press 1 to confirm, or press 2 to exit."))
#     if new_product == 1:
#         products[product_for_user] = int(input("enter new price: "))
#     else:
#         print("good by")
# print(products)


# # excercise 14
# count = 0
# big = 0
# hige = ""
# students = [{"name": "David", "age": 20, "grade": 90},
#             {"name": "Moshe", "age": 22, "grade": 75},
#             {"name": "Dana", "age": 21, "grade": 100},
#             {"name": "Noa", "age": 19, "grade": 55},
#             {"name": "Avi", "age": 23, "grade": 82}]
# for student in students:
#     print(f"{student["name"]} {student["grade"]}")
#     if student["grade"] > big:
#         big = student["grade"]
#         hige = student["name"]

#     count += student["grade"]


# for student in students:
#     if student["grade"] > 80:
#         print(student["name"])

# print(count/len(students))
# print(hige)


# # excercise 15
# students = [{"name": "David", "age": 20, "grade": 90},
#             {"name": "Moshe", "age": 22, "grade": 75},
#             {"name": "Dana", "age": 21, "grade": 100},
#             {"name": "Noa", "age": 19, "grade": 55},
#             {"name": "Avi", "age": 23, "grade": 82}]
# students.append({"name": "shlomo", "age": 21, "grade": 105})
# students[2]["grade"] = 43
# students.remove({"name": "David", "age": 20, "grade": 90})
# print(students)


# # excercise 16
# new_a = 0
# new_b = 0
# new_c = 0
# classroom_ = []
# classroom = {"Class A": ["David", "Moshe", "Dana"],
#              "Class B": ["Noa", "Avi", "Michael"],
#              "Class C": ["Daniel", "Shir", "Yossi"]}
# for k, v in classroom.items():
#     classroom_.append(k)
#     if k == "Class A":
#         print(v)
#         new_a = len(v)

#     if k == "Class B":
#         v.append("Aiala")
#         new_b = len(v)
#     if k == "Class C":
#         v.remove("Shir")
#         naw_c = len(v)
# print(classroom_)
# print(f"Class A = {new_a} | Class B = {new_b} | Class C = {new_c}")


# # excercise 17
# count = []
# products = {"Laptop": {"price": 4500,        "stock": 10},
#             "Mouse": {"price": 80,        "stock": 50},
#             "Keyboard": {"price": 150,        "stock": 20}}
# print(products["Laptop"]["price"])
# print(products["Mouse"]["price"])
# print(products["Keyboard"]["price"])
# print(products["Laptop"]["stock"])
# print(products["Mouse"]["stock"])
# print(products["Keyboard"]["stock"])
# products["melafefon"] = {"price": 120, "stock": 3}
# for product, v in products.items():
#     if products[product]["price"] > 100:
#         count.append(product)
# print(count)


# # excercise 18
# c = 0
# count = 0
# sum_ = 0
# big = ""
# employees = [("David", "Development", 15000),
#              ("Moshe", "Marketing", 12000),
#              ("Dana", "Development", 18000),
#              ("Noa", "HR", 11000)]
# for employee in employees:
#     print(employee[0])
# for employee in employees:
#     if employee[1] == "Development":
#         print(employee[0])
# for employee in employees:
#     if employee[2] > count:
#         count = employee[2]
#         big = employee[0]
# print(big)
# for employee in employees:
#     sum_ += employee[2]
#     c += 1
# print(sum_/c)


# # excercise 19
# inventory = {"Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
# name_for_product = input("enter a name to the product: ")
# amount_for_product = int(input("enter a amount to the product: "))
# if not inventory.get(name_for_product):
#     print("product not in store.")
# else:
#     if amount_for_product > inventory[name_for_product]:
#         print("The quantity is too large.")
#     else:
#         inventory[name_for_product] -= amount_for_product
#         print(inventory)


# # excercise 20
# a = 0
# big = ""
# votes = {"David": 0,    "Moshe": 0,    "Dana": 0}
# while True:
#     name = input("enter a name stop to break: ")
#     if name == "stop":
#         break
#     votes[name] += 1
# print(votes)
# for k, v in votes.items():
#     if v > a:
#         a = v
#         big = k
# print(big)


# # excercise 21
# contact_person = {"shlomo": "0509723162"}
# while True:
#     pick = int(input("""
# 1. Add a contact.
# 2. Search for a contact.
# 3. Update a phone number.
# 4. Delete a contact.
# 5. View all contacts.
# 6. Exit.
# """))
#     if pick == 1:
#         contact_person[input("name")] = input("fone")
#     if pick == 2:
#         name_ = input("enter a name: ")
#         if contact_person.get(name_):
#             print(contact_person[name_])
#     if pick == 3:
#         name_ = input("enter a name: ")
#         if contact_person.get(name_):
#             new = input("enter a number fone new: ")
#             contact_person[name_] = new
#             print(contact_person[name_])
#     if pick == 4:
#         name_ = input("enter a name: ")
#         if contact_person.get(name_):
#             contact_person.pop(name_)

#     if pick == 5:
#         print(contact_person)
#     if pick == 6:
#         print("good by")
#         break


# # excercise 22
# products = [{"name": "Laptop", "price": 4500, "stock": 10},
#             {"name": "Mouse", "price": 80, "stock": 50},
#             {"name": "Keyboard", "price": 150, "stock": 2},
#             {"name": "Screen", "price": 900, "stock": 5}]

# while True:
#     pick = int(input("""
# ===== Store Management =====

# 1. Show all products
# 2. Add product
# 3. Search product
# 4. Update product price
# 5. Update product stock
# 6. Sell product
# 7. Show products by price
# 8. Show products with low stock
# 9. Show total inventory value
# 0. Exit
# """))
#     if pick == 1:
#         for product in products:
#             print(
#                 f"{product["name"]} = {product["price"]} $, amout = {product["stock"]}")
#     if pick == 2:
#         name = input("enter a name: ")
#         price = int(input("enter a price: "))
#         stock = int(input("enter a stok: "))

#         products.append({"name": name, "price": price, "stock": stock})
#         for product in products:
#             print(
#                 f"{product["name"]} = {product["price"]} $, amout = {product["stock"]}")
#     if pick == 3:
#         flag = False
#         name = input("enter a name: ")
#         for product in products:
#             if product["name"] == name:
#                 flag = True
#                 print(
#                     f"{product["name"]} = {product["price"]} $, amout = {product["stock"]}")
#         if not flag:
#             print("the product not in store: ")

#     if pick == 4:
#         flaf = False
#         name = input("enter a name: ")
#         for product in products:
#             if product["name"] == name:
#                 flag = True
#                 new_price = int(input("enter a new price: "))
#                 product["price"] = new_price
#                 print(
#                     f"{product["name"]} = {product["price"]} $, amout = {product["stock"]}")
#         if not flag:
#             print("the product not in store.")
#     if pick == 5:
#         flaf = False
#         name = input("enter a name: ")
#         for product in products:
#             if product["name"] == name:
#                 flag = True
#                 new_stock = int(input("enter a new stock: "))
#                 product["stock"] = new_stock
#                 print(
#                     f"{product["name"]} = {product["price"]} $, amout = {product["stock"]}")
#         if not flag:
#             print("the product not in store.")
#     if pick == 6:
#         flag = False
#         name = input("enter a name: ")
#         for product in products:
#             if product["name"] == name:
#                 if product["stock"] > 0:
#                     flag = True
#                     product["stock"] -= 1
#                     print(
#                         f"{product["name"]} = {product["price"]} $, amout = {product["stock"]}")
#         if not flag:
#             print("the product not in store.")

#     if pick == 7:
#         new = []
#         price = int(input("enter a price: "))
#         for product in products:
#             if product["price"] < price:
#                 new.append(product)
#         print(new)
#     if pick == 8:
#         new = []
#         for product in products:
#             if product["stock"] < 10:
#                 new.append(product)
#         print(new)

#     if pick == 9:
#         count = 0
#         for product in products:
#             count += (product["price"]*product["stock"])
#         print(count)

#     if pick == 0:
#         print("good by")
#         break
