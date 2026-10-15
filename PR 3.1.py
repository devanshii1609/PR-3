# STUDENT DATA ORGANISER

students = {
    "Riya": 85,
    "Ishika": 92,
    "Devanshi": 88,
    "Parth": 79
}


def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")


def display_students():
    print("\n--- Student List ---")
    if students:
        for name, marks in students.items():
            print(f"{name} : {marks}")
    else:
        print("No student records found.")


def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        print(f"{name} scored {students[name]} marks.")
    else:
        print("Student not found.")


def update_marks():
    name = input("Enter student name: ")

    if name in students:
        new_marks = int(input("Enter new marks: "))
        students[name] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found.")


def remove_student():
    name = input("Enter student name to remove: ")

    if name in students:
        del students[name]
        print("Student removed successfully!")
    else:
        print("Student not found.")


def show_statistics():
    if students:
        marks = list(students.values())

        print("\n--- Statistics ---")
        print("Total Students:", len(students))
        print("Highest Marks:", max(marks))
        print("Lowest Marks:", min(marks))
        print("Average Marks:", round(sum(marks) / len(marks), 2))
    else:
        print("No student records available.")


def string_operations():
    name = input("Enter a student name: ")

    print("\n--- String Operations ---")
    print("Uppercase:", name.upper())
    print("Lowercase:", name.lower())
    print("Length:", len(name))
    print("Title Case:", name.title())


while True:
    print("""
========= STUDENT DATA ORGANISER =========
1. Add Student
2. Display Students
3. Search Student
4. Update Marks
5. Remove Student
6. Statistics
7. String Operations
8. Exit
==========================================
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        remove_student()

    elif choice == "6":
        show_statistics()

    elif choice == "7":
        string_operations()

    elif choice == "8":
        print("Thank you for using Student Data Organiser!")
        break

    else:
        print("Invalid choice. Please try again.")
