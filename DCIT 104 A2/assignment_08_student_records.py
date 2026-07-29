# ===============================================
# PROGRAMMING FUNDAMENTALS - Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# Student Record Management System
# ===============================================

students = []


def add_student():
    """Add a new student record."""
    name = input("Student name: ")
    student_id = input("Student ID: ")

    num_scores = int(input("How many scores? "))

    scores = []

    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)

    print(f'Student "{name}" added successfully.\n')


def display_students():
    """Display all student records."""

    if len(students) == 0:
        print("No student records found.\n")
        return

    print("-" * 70)
    print(f"{'Name':20} {'ID':12} {'Scores':20} {'Average'}")
    print("-" * 70)

    for student in students:
        average = sum(student["scores"]) / len(student["scores"])
        scores = ", ".join(str(int(score)) if score == int(score) else str(score)
                           for score in student["scores"])

        print(f"{student['name']:20} {student['id']:12} {scores:20} {average:.2f}")

    print("-" * 70)
    print()


def calculate_average():
    """Calculate average score for a specific student."""

    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            average = sum(student["scores"]) / len(student["scores"])
            print(f"{student['name']}'s average score: {average:.2f}\n")
            return

    print("Student ID not found.\n")


def menu():
    """Display the menu."""

    print("=" * 30)
    print("STUDENT RECORD SYSTEM MENU")
    print("=" * 30)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    while True:
        menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            calculate_average()

        elif choice == "4":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.\n")


main()