employees = {}

while True:
    print("\n1. Add Employee")
    print("2. Search Employee")
    print("3. View All")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        employees[emp_id] = name

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print("Employee Name:", employees[emp_id])
        else:
            print("Employee Not Found")

    elif choice == "3":
        for emp_id, name in employees.items():
            print(emp_id, ":", name)

    elif choice == "4":
        break
