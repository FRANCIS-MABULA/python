# Student Grading System
# ICT111 - Principles of Programming

students = []


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty. Please try again.")


def get_mark():
    while True:
        try:
            mark = float(input("Enter student's mark (0-100): ").strip())
            if 0 <= mark <= 100:
                return mark
            print("Error: Mark must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")


def assign_grade(mark):
    if mark >= 80:
        return "A", "Excellent"
    elif mark >= 70:
        return "B", "Very good"
    elif mark >= 60:
        return "C", "Good"
    elif mark >= 50:
        return "D", "Pass"
    else:
        return "F", "Fail"


def add_student():
    print("\n--- ADD STUDENT ---")
    student_number = get_non_empty_text("Enter student number: ")

    for student in students:
        if student["student_number"] == student_number:
            print("Error: A student with that number is already registered.")
            return

    name = get_non_empty_text("Enter student's name: ")
    mark = get_mark()
    grade, decision = assign_grade(mark)

    student = {
        "student_number": student_number,
        "name": name,
        "mark": mark,
        "grade": grade,
        "decision": decision
    }
    students.append(student)

    print("\nStudent added successfully.")
    print(f"Name: {name}")
    print(f"Mark: {mark:g}")
    print(f"Grade: {grade}")
    print(f"Decision: {decision}")


def display_students():
    print("\n--- STUDENT RECORDS ---")
    if not students:
        print("No student records are available.")
        return

    print("-" * 78)
    print(f"{'STUDENT NUMBER':<18}{'NAME':<24}{'MARK':>8}{'GRADE':>10}{'DECISION':>16}")
    print("-" * 78)

    for student in students:
        print(
            f"{student['student_number']:<18}"
            f"{student['name']:<24}"
            f"{student['mark']:>8.2f}"
            f"{student['grade']:>10}"
            f"{student['decision']:>16}"
        )
    print("-" * 78)


def class_summary():
    print("\n--- CLASS SUMMARY ---")
    if not students:
        print("No student records available. Add students before viewing statistics.")
        return

    marks = [student["mark"] for student in students]
    total_students = len(students)
    total_marks = sum(marks)
    average_mark = total_marks / total_students
    highest_mark = max(marks)
    lowest_mark = min(marks)

    passes = 0
    fails = 0

    for student in students:
        if student["mark"] >= 50:
            passes += 1
        else:
            fails += 1

    print(f"Number of students : {total_students}")
    print(f"Total marks        : {total_marks:g}")
    print(f"Average mark       : {average_mark:.2f}")
    print(f"Highest mark       : {highest_mark:g}")
    print(f"Lowest mark        : {lowest_mark:g}")
    print(f"Number of passes   : {passes}")
    print(f"Number of failures : {fails}")


def main():
    while True:
        print("\n" + "=" * 42)
        print("          STUDENT GRADING SYSTEM")
        print("=" * 42)
        print("1. Add student")
        print("2. Display all students")
        print("3. Class summary")
        print("4. Exit")
        print("=" * 42)

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            class_summary()
        elif choice == "4":
            print("\nThank you for using the Student Grading System.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
