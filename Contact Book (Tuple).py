contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")

        contact = (name, phone)
        contacts.append(contact)

    elif choice == "2":
        for name, phone in contacts:
            print(f"Name: {name}, Phone: {phone}")

    elif choice == "3":
        break
