from functools import reduce

salaries = [25000, 40000, 35000, 20000, 50000]

high_salary = list(filter(lambda x: x > 30000, salaries))

updated_salary = list(map(lambda x: x * 1.10, high_salary))

total_salary = reduce(lambda x, y: x + y, updated_salary)

print("High Salaries:", high_salary)
print("After Increment:", updated_salary)
print("Total Expense:", total_salary)
