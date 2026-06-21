from functools import reduce

# Student marks
marks = [45, 78, 32, 90, 56, 28, 67, 81]

print("Original Marks:")
print(marks)

# Filter: Students who passed (>= 35)
passed_students = list(filter(lambda x: x >= 35, marks))

print("\nPassed Students:")
print(passed_students)

# Map: Add 5 bonus marks
bonus_marks = list(map(lambda x: x + 5, passed_students))

print("\nMarks After Bonus:")
print(bonus_marks)

# Reduce: Calculate total marks
total_marks = reduce(lambda x, y: x + y, bonus_marks)

print("\nTotal Marks:", total_marks)

# Average marks
average_marks = total_marks / len(bonus_marks)

print("Average Marks:", round(average_marks, 2))
