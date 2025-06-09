fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)


#### Average Height ####
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height = 0

# for height in student_heights:
#     total_height += height
# print(total_height)

# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)


#### High Score ####
# student_scores = input("Input a list of student score => ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# heighest_score = 0

# for score in student_scores:
#     if score > heighest_score:
#         heighest_score = score
# print(f"The heightest score in the class is : {heighest_score}")


#### For loop with range
# for number in range(1,11,3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# total1 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total1 += number

# print(total1)

# total2 = 0
# for number in range(2, 101, 2):
#     total2 += number
# print(total2)


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
