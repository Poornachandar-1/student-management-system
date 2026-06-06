students = {}
while True:
    print("1. Add Student: ")
    print("2. View Students: ")
    print("3. Search Students: ")
    print("4. Delete Student: ")
    print("5. Exit: ")
    choice = input("Enter your choice: ")
    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")
        students[name] = marks
        print("Student added successfully!")
    # View Students
    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(name, ":", marks)
        else:
            print("Student not found!")
    # Search Students
    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in students:
            print("Student found: ", name, ":", students[name])
        else:
            print("Student not found!")
    # Delete Student
    elif choice == "4":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found!")
    # Exit 
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")