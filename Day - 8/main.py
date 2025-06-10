import math

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# greet_with_name("Bhavya")


# function with more then 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}?")


# greet_with(location="London", name="Bhavya")


# Challenge 1
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area / cover)
#     print(f"You'll need {num_of_cans} cans of paint")


# test_h = int(input("Height of wall : "))
# test_w = int(input("Width of wall : "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime Number
def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number.")


n = int(input("Check this number => "))
prime_checker(number=n)
