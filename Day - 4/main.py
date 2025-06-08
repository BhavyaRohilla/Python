import random

# random.seed(123)


# random_integer = random.randint(1, 10)
# random_float = random.random() * 5
# print(random_integer, random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# indian_states = [
#     "Andhra Pradesh",
#     "Arunachal Pradesh",
#     "Assam",
#     "Bihar",
#     "Chhattisgarh",
#     "Goa",
#     "Gujarat",
#     "Haryana",
#     "Himachal Pradesh",
#     "Jharkhand",
#     "Karnataka",
#     "Kerala",
#     "Madhya Pradesh",
#     "Maharashtra",
#     "Manipur",
#     "Meghalaya",
#     "Mizoram",
#     "Nagaland",
#     "Odisha",
#     "Punjab",
#     "Rajasthan",
#     "Sikkim",
#     "Tamil Nadu",
#     "Telangana",
#     "Tripura",
#     "Uttar Pradesh",
#     "Uttarakhand",
#     "West Bengal",
# ]


# print(indian_states[0])


# test_seed = int(input)

nameAsCSV = input("Give me the everybody's names, sepersted by a comma => ")
names = nameAsCSV.split(", ")

# x = len(names)
# random_choice = random.randint(0, x - 1)
# person_who_will_pay = names[random_choice]

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")
