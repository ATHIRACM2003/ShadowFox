#Task 4 - If

#1. BMI Calculation
height = float(input("Enter Height in meters: "))
weight = float(input("Enter Weight in kilograms: "))
bmi = (weight)/(height*height)
if bmi >= 30:
    print("\nObesity")
elif bmi>25 and bmi<=29:
    print("\nOverweight")
elif bmi>18.5 and bmi<=25:
    print("\nNormal")
elif bmi<18.5:
    print("Underweight")
else:
    print("Invalid Entry")

