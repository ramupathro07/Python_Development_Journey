visitors = set()

while True:
    print("\n1. Add Visitor")
    print("2. View Unique Visitors")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter visitor name: ")
        visitors.add(name)

    elif choice == "2":
        print("Unique Visitors:")
        for visitor in visitors:
            print(visitor)

    elif choice == "3":
        break
