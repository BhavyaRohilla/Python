import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*()_+-=[]{}|;:',.<>?/")
# 1️⃣ Take input from user
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))


# Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

# Hard Level
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your Yum Yum and Powerfull password is => {password}")
