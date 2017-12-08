#CTI 110
#M2HW2 - Tip, Tax, and Total
#Zachary Burkhardt
#9/10/17

print("Input your meal cost to find your tip, tax, and total")
meal_cost = float(input("Meal cost: "))
tip = meal_cost * 0.18
print("Tip is", tip)
tax = meal_cost * 0.07
print("Tax is", tax)
total_cost = meal_cost + tip + tax
print("Your total cost is", total_cost)
