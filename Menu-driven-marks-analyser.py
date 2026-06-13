marks = []

def menu():
    print("\n--- Student Marks Analyzer ---")
    print("1. Add Marks")
    print("2. View Marks")
    print("3. Analyze")
    print("4. Exit")

while True:
    menu()
    choice = int(input("Enter choice: "))

    if choice == 1:
        m = int(input("Enter marks: "))
        marks.append(m)

    elif choice == 2:
        print("Marks:", marks)

    elif choice == 3:
        if not marks:
            print("No data available!")
            continue
        
        avg = sum(marks) / len(marks)
        print("Average:", avg)
        print("Highest:", max(marks))
        print("Lowest:", min(marks))
        print("Passed:", len([m for m in marks if m >= 50]))
        print("Failed:", len([m for m in marks if m < 50]))

    elif choice == 4:
        break


    else:
        print("Invalid choice!")
