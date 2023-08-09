print("Welcome to the python pizza deliveries!")

s = 15
m = 20
l = 25


size = input("What size of pizza do you want? S, M or L: ").lower()
add_pepperoni = input("Would you like to add Pepperoni? Y or N: ").lower()
add_cheese = input("Would you like to add extra cheese? Y or N: ").lower()

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    elif size == "m" or size == "l":
        bill += 3

if add_cheese == "y":
    bill += 1

print(f"Your final bill is: {bill}")


