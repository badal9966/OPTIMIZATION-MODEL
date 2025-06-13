# Task 4: Business Optimization using PuLP (Diet Problem Example)

from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Define problem
model_opt = LpProblem(name="diet-problem", sense=LpMaximize)

# Variables: quantities of food items
x1 = LpVariable(name="food_A", lowBound=0)
x2 = LpVariable(name="food_B", lowBound=0)

# Objective function: maximize nutrition (simplified)
model_opt += 50 * x1 + 40 * x2, "Total Nutritional Value"

# Constraints: cost limit and calories
model_opt += 3 * x1 + 2 * x2 <= 12, "Cost Limit"
model_opt += 500 * x1 + 300 * x2 >= 2000, "Calorie Requirement"

# Solve
model_opt.solve()

# Results
print(f"Optimal food_A: {x1.value()}")
print(f"Optimal food_B: {x2.value()}")
print(f"Total Nutrition: {model_opt.objective.value()}")

print("Task 4 Complete: Optimization problem solved with PuLP.")
