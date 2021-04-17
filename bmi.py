print("BMI Calculator\n")

name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (mtr): "))

bmi = weight / (height * height)

if bmi <= 18.5:
    print('\nYour BMI is', bmi, 'which means you are underweight')

elif 18.5 < bmi < 25:
    print('\nYour BMI is', bmi,'which means you are normal')

elif 25 < bmi < 30:
    print('\nyour BMI is', bmi,' which means you are overweight')

elif bmi > 30:
    print('\nYour BMI is', bmi,'which means you are obese')