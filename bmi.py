# M1L6 Activity 3
# Topic: BMI Checker
# This program calculates BMI and checks the BMI category

weight = 60      # in kilograms
height = 1.65    # in meters

bmi = weight / (height * height)

print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")

# End of program
