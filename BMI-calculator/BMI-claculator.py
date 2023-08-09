print("Welcome to the BMI calculator!")

height = float(input("Enter your height in m: "))

weight = float(input("Enter your weight in kg: "))
pounds = round(weight * 2.2, 2)
print(f"weight in pounds: {pounds}")

BMI = round(float(weight/height ** 2), 2)

if BMI >= 35:
    print(f"Your BMI is {BMI}. You're extremely obese! You should talk to your doctor about the concerns!")
elif BMI >= 30:
    print(f"Your BMI is {BMI}. You're Obese!")
elif BMI >= 25:
    print(f"Your BMI is {BMI}. You're Overweight.")
elif BMI >= 18.5:
    print(f"Your BMI is {BMI}. You have normal weight.")
elif BMI < 18.5:
    print(f"Your BMI is {BMI}. You are underweight")