print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill?: "))

people = int(input("How many people to split the bill?: "))

tip_percentage = int(input("What percentage tip would you like to give? 10,12 or 15?: "))

amount = float(total_bill * tip_percentage/100 + total_bill)

amount_per_person = amount/people

print(f"Each person should pay: ${amount_per_person}")