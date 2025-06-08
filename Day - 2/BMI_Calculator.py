height = input("Enter Your height in m => ")
weight = input("Enter Your weight in kg => ")

BMI = int(weight) / float(height) ** 2
bmi_as_int = int(BMI)

print(bmi_as_int)
