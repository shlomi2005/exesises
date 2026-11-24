# # excercise 1

# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])

# # excercise 2
# students = ["shlomo", "yoshf", "moshe"]
# print(students)
# print(len(students))
# print(students[0], students[-1])
# students[1] = "yakov"
# print(students)


# # excercise 3
# grade = [95, 97, 93, 100, 99]
# grade.append(89)
# grade.insert(0, 94)
# grade[2] = 93
# print(grade)


# # excercise 4
# numbers = [2, 4, 6, 5, 7, 6, 8, 3, 2, 9]
# print(numbers)
# numbers.pop(0)
# print(numbers)
# numbers.pop(-1)
# print(numbers)
# numbers.pop(2)
# print(numbers)


# # excercise 5
# products = ["pen", "leptop", "cucumber", "tomato"]
# if "leptop" in products:
#     print("The product has been found")
# if "lop" not in products:
#     print("The product not in been found")


# # excercise 6
# numbers = [2, 3, 5, 4, 8, 6, 5, 7, 8, 9]
# for num in numbers:
#     print(num)


# # excercise 7
# numbers = [2, 3, 5, 4, 8, 6, 5, 7, 8, 9]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)


# # excercise 8
# grades = [95, 97, 93, 100, 99]
# total = 0
# for grad in grades:
#     total += grad
# print(total)


# # excercise 9
# maxi = 0
# numbers = [2, 3, 5, 4, 8, 6, 5, 7, 10, 9]
# for num in numbers:
#     if num > maxi:
#         maxi = num
# print(maxi)


# # excercise 10
# flag = False
# students = ["shlomo", "yoshf", "moshe"]
# name = input("enter your name: ")
# for student in students:
#     if student == name:
#         flag = True
# if flag:
#     print("found")
# else:
#     print("not found")


# # excercise 11

# numbers = [2, 3, 5, 4, 8, 6, 5, 7, 10, 9]
# num_user = int(input("enter a number: "))
# for i, num in enumerate(numbers):
#     if num == num_user:
#         print(i)


# # excercise 12

# count = 0
# numbers = [2, 3, 5, 48, 87, 65, 5, 7, 10, 9]
# for num in numbers:
#     if num > 50:
#         count += 1
# print(count)


# # excercise 13
# numbers = [2, 3, 5, 48, 87, 65, 5, 7, 10, 9]
# new_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         new_numbers.append(num)
# print(new_numbers)


# # excercise 14

# students = ["shlomo", "yoshf", "moshe", "yakov"]
# count = 1
# while count < len(students)+1:
#     print(count, students[count-1])
#     count += 1


# # excercise 15
# numbers = [2, 3, 5, 48, 87, 65, 5, 7, 10, 9]
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[2:7])
# print(numbers[::-1])


# # excercise 16
# students = ["shlomo", "yoshf", "moshe", "yakov",
#             "david", "ariel", "yaeir", "nama", "reut", "shilat"]
# print(students[::2])
# print(students[1::2])
# print(students[::-2])


# # excercise 17
# numbers = [2, 3, 5, 48, 87, 65, 5, 7, 10,
#            9, 22, 32, 3, 43, 4, 12, 43, 54, 3, 23]

# new = numbers[:10]
# new1 = numbers[10:]
# new2 = numbers[4:14]
# print(new)
# print(new1)
# print(new2)


# # excercise 18
# numbers = [2, 3, 5, 48, 87, 65, 5, 7, 10,
#            9, 22, 32, 3, 43, 4, 12, 43, 54, 3, 23]
# new = numbers[:len(numbers)//2]
# new2 = numbers[len(numbers)//2:]
# print(new)
# print(new2)


# # excercise 19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new = [num * 2 for num in numbers]
# new1 = [num ** 2 for num in numbers]
# new2 = [num for num in numbers if num % 2 == 0]
# new3 = [num for num in numbers if num > 5]
# print(new)
# print(new1)
# print(new2)
# print(new3)


# # excercise 20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# new_grades = [num for num in grades if num >= 60]
# new_grades2 = [num for num in grades if num < 60]
# new_grades3 = [num + 5 for num in grades]
# print(new_grades)
# print(new_grades2)
# print(new_grades3)


# # excercise 21
# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# new = [name for name in names if len(name) > 4]
# new2 = [name.upper() for name in names]
# new3 = [name for name in names if name[0] == "D"]
# print(new)
# print(new2)
# print(new3)


# # excercise 22
# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new = [num for num in numbers if num % 3 == 0 and num > 10]
# print(new)


# # excercise 23
# new = []
# count = 0
# for i in range(10):
#     num = int(input("enter a number: "))
#     new.append(num)
# print(new)
# for num in new:
#     if num > count:
#         count = num
# print(count)
# count = new[0]
# for num in new:
#     if num < count:
#         count = num

# print(count)
# count = len(new)
# n = 0
# for num in new:
#     n += num
# print(n/count)


# # excercise 24
# flag = False
# users = ["Moshe", "David", "Dana", "Noa", "Michael"]
# name_ = input("enter name: ")
# for name in users:
#     if name == name_:
#         flag = True
#         users.remove(name)
# if flag:
#     print("delete")
# else:
#     print("name not in list")


# # excercise 25
# numbers = [2, 3, 5, 48, 87, 65, 5, 7, 10, 9]
# new = [num for num in numbers if num % 2 == 0]
# new1 = [num for num in numbers if num % 2 != 0]
# new2 = [num for num in numbers if num > 20]
# print(new)
# print(new1)
# print(new2)


# # excercise 26
# count = 0
# flag = False
# numbers = [2, 3, 5, 48, 87, 65, 5, 7, 10, 9]
# num_user = int(input("enter a number"))
# for num in numbers:
#     if num == num_user:
#         count += 1
#         flag = True

#     elif num != num_user:
#         count = count
# if not flag:
#     print("number not in list")
# else:

#     print(count)


# # excercise 27
# numbers_1 = [2, 3, 5, 48, 87, 65, 5, 7, 10, 9]
# numbers_2 = [2, 3, 5, 48, 87, 65, 5, 7, 10, 9]
# new = numbers_1+numbers_2
# print(new)
# print(new[:5])
# print(new[-5:])
# print(new[::-1])


# # excercise 28
# flag = True
# numbers = [2, 3, 5, 48, 87, 65, 5, 7, 10, 9]
# num_user = int(input("enter a number"))
# for num in numbers:
#     if num == num_user:
#         flag = False
# if flag:
#     numbers.append(num_user)
# print(numbers)


# # excercise 29

# grades = [85, 72, 90, 55, 100, 63, 48, 77]

# while True:
#     pick = int(input("""
# ===== Grades Management =====

# 1. Show all grades
# 2. Add a grade
# 3. Search for a grade
# 4. Remove a grade
# 5. Show passing grades
# 6. Show failing grades
# 7. Show highest and lowest grade
# 8. Show average grade
# 9. Show first 3 grades
# 10. Show grades in reverse
# 0. Exit
#  """))
#     if pick == 1:
#         for grade in grades:
#             print(grade)
#     if pick == 2:
#         new = int(input("enter a grade: "))
#         grades.append(new)
#     if pick == 3:
#         search = int(input("enter a grade Search: "))
#         for i, grade in enumerate(grades):
#             if grade == search:
#                 print(i)
#     if pick == 4:
#         remov = int(input("enter a grade the you wont remov: "))
#         grades.remove(remov)
#     if pick == 5:
#         new_list = [num for num in grades if num > 60]
#         print(new_list)
#     if pick == 6:
#         new_list2 = [num for num in grades if num < 60]
#         print(new_list2)
#     if pick == 7:
#         hige = 0
#         low = grades[0]
#         for num in grades:
#             if num > hige:
#                 hige = num
#             if num < low:
#                 low = num
#         print(f"hige = {hige}, low = {low}")
#     if pick == 8:
#         count = 0
#         gr = 0
#         for num in grades:
#             gr += num
#             count += 1
#         print(gr/count)
#     if pick == 9:
#         print(grades[:3])
#     if pick == 10:
#         print(grades[::-1])
#     if pick == 11:
#         break
