# print("Welcome to the rollercoaster!!!!")
# height = int(input("What is you height in cm? => "))

# if height > 120:
#     print("You can ride the roller coaster!!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# Odd / Even

# number = int(input("Enter the number you have to check => "))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number id odd")


print("Welcome to the rollercoaster!!!!")
height = int(input("What is your height in cm? => "))
bill = 0

if height > 120:
    print("You can ride the roller coaster!!")
    age = int(input("Enter your age => "))

    if age < 12:
        bill = 5
        print("Child tickets are: $5")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    elif age > 18:
        bill = 12
        print("Adult tickets are: $12")
    else:
        bill = 7
        print("Teen tickets are: $7")

    wants_photo = input("Do you want a photo taken? Y or N => ").strip().upper()
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
