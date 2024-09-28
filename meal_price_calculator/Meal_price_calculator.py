# Meal Price Calculator

child_meal = float(input("what is the price of a child's meal? "))
adult_meal = float(input("what is the price of an adult's meal? "))
num_children = int(input("what is the number of children? "))
num_adults = int(input("what i sthe number of adults? "))

# Meal Subtotal
meal_subtotal = num_children * child_meal + adult_meal * num_adults
print((f'meal subtotal is {meal_subtotal}'))

# Use the value below to represent the variables
# Child's meal 4.50
# Adults meal 9.00
# Number of children 4
# Number of adults 2