# ICT111 LAB 2: STUDENT GRADING SYSTEM

# Store all student records
students = []

while True:
    print("\n===== STUDENT GRADING SYSTEM =====")
    print("1. Add student")
    print("2. Display all students")
    print("3. Class summary")
    print("4. Exit")

    option = input("Choose an option (1-4): ")

    # OPTION 1: ADD STUDENT
    if option == "1":

        # Validate student number
        while True:
            student_number = input("Enter student number: ").strip()

            if student_number == "":
                print("Error: Student number cannot be blank.")
            else:
                break

        # Validate student name
        while True:
            name = input("Enter student name: ").strip()

            if name == "":
                print("Error: Student name cannot be blank.")
            else:
                break

        # Validate student mark
        while True:
            try:
                mark = float(input("Enter student mark (0-100): "))

                if mark < 0 or mark > 100:
                    print("Error: Mark must be between 0 and 100.")
                else:
                    break

            except ValueError:
                print("Invalid input! Enter a numeric mark.")

        # Assign grade and decision
        if mark >= 80:
            grade = "A"
            decision = "Excellent"

        elif mark >= 70:
            grade = "B"
            decision = "Very good"

        elif mark >= 60:
            grade = "C"
            decision = "Good"

        elif mark >= 50:
            grade = "D"
            decision = "Pass"

        else:
            grade = "F"
            decision = "Fail"

        # Store student information in a dictionary
        student = {
            "student_number": student_number,
            "name": name,
            "mark": mark,
            "grade": grade,
            "decision": decision
        }

        students.append(student)

        print("\nStudent added successfully!")
        print("Assigned Grade:", grade)
        print("Decision:", decision)

    # OPTION 2: DISPLAY ALL STUDENTS
    elif option == "2":

        if len(students) == 0:
            print("No student records available.")

        else:
            print("\n===== STUDENT RECORDS =====")

            for student in students:
                print("----------------------------")
                print("Student Number:", student["student_number"])
                print("Name:", student["name"])
                print("Mark:", student["mark"])
                print("Grade:", student["grade"])
                print("Decision:", student["decision"])

    # OPTION 3: CLASS SUMMARY
    elif option == "3":

        if len(students) == 0:
            print("No students available for class summary.")

        else:
            total_students = 0
            total_marks = 0
            highest_mark = students[0]["mark"]
            lowest_mark = students[0]["mark"]
            passes = 0
            fails = 0

            for student in students:
                mark = student["mark"]

                total_students += 1
                total_marks += mark

                if mark > highest_mark:
                    highest_mark = mark

                if mark < lowest_mark:
                    lowest_mark = mark

                if mark >= 50:
                    passes += 1
                else:
                    fails += 1

            average = total_marks / total_students

            print("\n===== CLASS SUMMARY =====")
            print("Total Students:", total_students)
            print("Class Average:", round(average, 2))
            print("Highest Mark:", highest_mark)
            print("Lowest Mark:", lowest_mark)
            print("Total Passes:", passes)
            print("Total Fails:", fails)

    # OPTION 4: EXIT
    elif option == "4":
        print("Thank you for using the grading system.")
        break

    # INVALID MENU OPTION
    else:
        print("Invalid option! Please choose between 1 and 4.")