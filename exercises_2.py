# # excercise 1
num1 = 25
num2 = 7
print(
    f"""
addition = {num1 + num2}
subtraction = {num1 - num2}
multiplication = {num1 * num2}
Division = {num1 / num2}
integer_division = {num1 // num2}
remainder_division = {num1 % num2}
holding = {num1 ** num2}
""")


# excercise 2
balance = 1000
print(balance)
balance += 250
print(balance)
balance -= 100
print(balance)
balance *= 2
print(balance)
balance /= 4
print(balance)


# excercise 3
price = int(input("enter a price for product: "))
discount_percentage = int(input("enter a Discount Percentage: "))
total_discount = price * discount_percentage / 100
total_price = price-total_discount
print(total_discount)
print(total_price)

# excercise 4
sum_of_money = int(input("enter a sum_of_money: "))
annual_interest_rate = int(input("enter a annual_interest_rate: "))
total_interest = sum_of_money * annual_interest_rate / 100
total_price = sum_of_money + total_interest
print(total_interest)
print(total_price)


# excercise 5
grade1 = float(input("enter a greate 1: "))
grade2 = float(input("enter a greate 2: "))
grade3 = float(input("enter a greate 3: "))
average = (grade1+grade2+grade3)/3
print(average)


# excercise 6

first_name = "David"
last_name = "Cohen"
city = "Tel Aviv"
print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")


# excercise 7
name = input("enter a full name: ")
print(name)
print(len(name))
print(name.upper())
print(name.lower())

# excercise 8
sentence = input("enter a sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.title())


# excercise 9
name = input("enter a full name: ")
print(name)
print(name.strip())
print(len(name))
print(len(name.strip()))


# excercise 10
sentence = "I love Java programming"
print(sentence.replace("Java", "Python"))
print(sentence.count("love"))
print(sentence.startswith("I"))
print(sentence.endswith("programming"))


# excercise 11
word = "Programming"
print(word[0])
print(word[-1])
print(word[2])
print(word[:3])
print(word[-4:])
print(word[::-1])


# excercise 12
a = "100"
b = "25"
c = 10
d = 5.5
a = int(a)
b = float(b)
c = str(c)
d = int(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# excercise 13
age = int(input("Enter your age: "))
print(age + 10)


# excercise 14
VAT = 18
Product_price_before_vat = float(input("enter a product_price_before_vat: "))
price_including_vat = Product_price_before_vat * VAT/100
total_price = Product_price_before_vat + price_including_vat
print(total_price)


# excercise 15
name = input("enter a first name: ")
last_name = input("enter a last name: ")
len_ = len(name)+len(last_name)
age = int(input("enter a age: "))
monthly_salary = int(input("enter a monthly_salary: "))
number_seniority = int(input("enter a number of years of seniority: "))
annual_salary = monthly_salary*number_seniority
annual_salary_5 = annual_salary*1.05
print(f"""
================================
    EMPLOYEE DETAILS SYSTEM
================================

employee: {name} {last_name}
Age: {age}
monthly_salary: {monthly_salary}
Number_seniority: {number_seniority}
annual_salary: {annual_salary}
Monthly annual_salary_5: {round(annual_salary_5, 2)}

================================
    EMPLOYEE DETAILS SYSTEM
================================
""")

print(len_)


# excercise 16
amount = float(input("enter a amount ₪: "))
usd_rate = 3.25
total_dolars = amount / usd_rate
total_iros = amount / 3.75
total_amout_dolars = total_dolars*1.02
total_amout_iros = total_iros*1.02
print(total_amout_dolars)
print(total_amout_iros)


# excercise 17
name = input("enter a first name: ")
last_name = input("enter a last name: ")
year_birth = int(input("enter a year of birth: "))
email = f"{name}.{last_name}.{year_birth}@gmail.com"
print((email.lower()))


# excercise 18
sentence = input("enter a sentence: ")
print(sentence)
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence[::-1])
print(sentence.count("a"))
print(sentence.replace(" ", "-"))

# Summary Task
name = input("enter your name: ")
product = input("enter a name for product: ")
price_product = int(input("enter a pprice for product: "))
quantity = int(input("enter a quantity the products: "))
discount_percentage = int(input("enter a discount percentage: "))
discount_vat = int(input("enter a discount vat: "))
subtotal = price_product*quantity
discount = subtotal*discount_percentage/100
after_discount = subtotal-discount
vat_Amount = subtotal*discount_vat/100
total = after_discount + vat_Amount
print(f"""
================================
        PURCHASE INVOICE
================================

Customer: {name}
Product: {product}

Unit Price: {price_product}
Quantity: {quantity}

Subtotal: {subtotal}
Discount: {discount}
After Discount: {after_discount}

VAT: {discount_vat}%
VAT Amount: {vat_Amount}

TOTAL: {total}

================================
    THANK YOU FOR SHOPPING
================================
""")
