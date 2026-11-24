# # excercise 1

# number = 0
# while number < 10:
#     number += 1
#     print(number)


# # excercise 2
# number = 11
# while number > 0:
#     number -= 1
#     print(number)
# print("START!")


# # excercise 3
# num = 1
# while num < 51:
#     if num % 2 == 0:
#         print(num)
#     num += 1


# # excercise 4
# num = int(input("enter a number"))
# count = 1
# while count < 5:
#     print(num*count)
#     count += 1


# # excercise 5
# num = 0
# count = 100
# while count >= 1:
#     num += count

#     count -= 1
# print(num)


# # excercise 6
# while True:
#     password = input("enter your password: ")
#     if password == "Python123":
#         print("Welcome!")
#         break


# # excercise 7

# secret_number = 27
# while True:
#     num_user = int(input("Guess the number: "))
#     if num_user == secret_number:
#         print("welcome!")
#         break


# # excercise 8
# count = 0
# while True:
#     num = int(input("enter a number 0 to break: "))
#     if num != 0:
#         count += num
#     else:
#         print(count)
#         break


# # excercise 9
# count = 0
# num = 0
# while True:
#     grades = int(input("Enter your grades; 999 to exit"))
#     if grades == 999:
#         break
#     num += 1
#     count += grades
# print(count)
# print(count/num)

# # excercise 10
# count = 0
# num = 0
# while True:
#     number = int(
#         input("Enter numbers a negative number will trigger an exit: "))
#     if number < 0:
#         break
#     count += number
#     num += 1
# print(count)
# print(num)


# # excercise 11
# count = 1
# num = int(input("enter a number: "))
# while count < 11:
#     print(f"{num} * {count} = {num*count}")
#     count += 1


# # excercise 12
# count = 0
# num = int(input("enter a number: "))
# while num:
#     num //= 10
#     count += 1
# print(count)


# # excercise 13
# new_number = 0
# num_user = int(input("enter a number: "))
# while num_user:
#     number = num_user % 10
#     new_number = new_number * 10 + number
#     num_user //= 10
# print(new_number)


# # excercise 14
# num_user = int(input("enter a number: "))
# caount = 2
# flag = False
# while caount < num_user:
#     if num_user % caount == 0:
#         flag = True
#         break
#     caount += 1
# if flag:
#     print("not reshoni")
# else:
#     print("resoni")


# # excercise 15
# balance = 5000
# while True:
#     pick = int(input("""
# 1. Check balance.
# 2. To deposit money.
# 3. To withdraw money.
# 4. exit.
#     """))
#     if pick == 1:
#         print(balance)
#     if pick == 2:
#         deposit = int(input("How much money do you want to deposit?: "))
#         balance += deposit
#         print("The balance has been successfully changed. Your balance is now", balance)
#     if pick == 3:
#         withdraw = int(input("How much money would you like to withdraw?: "))
#         if withdraw > balance:
#             print("You cannot withdraw more than the balance.")
#         elif withdraw < 0:
#             print("The withdrawal amount must be positive.")
#         else:
#             balance -= withdraw
#             print(
#                 "The withdrawal was successful. The amount remaining in your account is", balance)
#     if pick == 4:
#         print("good bay")
#         break


# excercise 16
# count = 1
# while True:
#     if count < 16:
#         print(count)
#         count += 1
#     else:
#         break


# # excercise 17
# count = 1
# while count < 30:
#     if count % 3 == 0:
#         count += 1

#     else:
#         print(count)
#         count += 1


# # excercise 18
# while True:
#     num_user = int(input("enter a number: "))
#     if num_user == 100:
#         print("good loake")
#         break


# # excercise 19
# for i in range(1, 21):
#     print(i)


# # excercise 20
# for i in range(0, 101, 5):
#     print(i)


# # excercise 21
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)


# # excercise 22
# num = int(input("enter a number: "))
# for i in range(1, 11):
#     print(num*i)


# # excercise 23
# num1 = int(input("enter a number1: "))
# num2 = int(input("enter a numbe2: "))
# total = 0
# for i in range(num1, num2+1):
#     total += i
# print(total)


# # excercise 24
# for i in range(15, 100, 15):
#     print(i)


# # excercise 25
# lines = int(input("Number of lines"))
# columns = int(input("Number of columns"))
# for i in range(lines):
#     print("*"*columns)


# # excercise 26
# for i in range(1, 7):
#     for j in range(i):
#         print("*", end="")
#     print()


# # excercise 27
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")


# # excercise 28
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i},{j}")


# # excercise 29
# points = 0
# while True:
#     pick = int(input("""
# ===== MATH GAME =====

# 1. Start Game
# 2. View Instructions
# 3. Exit

# Choose:
# """))
#     if pick == 1:
#         points += 1 if int(input("1 + 1 = ")) == 2 else 0
#         points += 1 if int(input("1 + 2 = ")) == 3 else 0
#         points += 1 if int(input("1 + 3 = ")) == 4 else 0
#         points += 1 if int(input("1 + 4 = ")) == 5 else 0
#         points += 1 if int(input("1 + 5 = ")) == 6 else 0
#         points += 1 if int(input("1 + 6 = ")) == 7 else 0
#         points += 1 if int(input("1 + 7 = ")) == 8 else 0
#         points += 1 if int(input("1 + 8 = ")) == 9 else 0
#         points += 1 if int(input("1 + 9 = ")) == 10 else 0
#         points += 1 if int(input("1 + 10 = ")) == 11 else 0
#         print(points)
#     if pick == 2:
#         print(points)
#     if pick == 3:
#         break
