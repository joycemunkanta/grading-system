# STUDENT GRADING SYSTEM

## MULUNGUSHI UNIVERSITY
**School:** Engineering and Technology  
**Department:** Computer Science and IT  
**Course:** ICT111 – Principles of Programming (Python & Git)  
**Lab:** Student Grading System
**name** joyce chungu munkanta
**student no** 202602328
**program** computer science 

---

## 1. PROJECT DESCRIPTION

The Student Grading System is a console-based Python application designed to record student information, calculate grades and generate class statistics.

The system allows users to:
- Add student records.
- Assign grades automatically.
- Display all student records.
- Calculate class statistics.
- Validate student marks and information.

## 2. INPUT–PROCESS–OUTPUT (IPO)

### Input
- Student number
- Student name
- Student mark

### Process
1. Validate student information.
2. Check that marks are between 0 and 100.
3. Assign grades using if, elif and else.
4. Store records using lists and dictionaries.
5. Calculate class statistics.

### Output
- Student details.
- Assigned grades and decisions.
- Total number of students.
- Class average.
- Highest and lowest marks.
- Total passes and fails.

## 3. GRADING SCALE

| Marks | Grade | Decision |
|---|---|---|
| 80–100 | A | Excellent |
| 70–79 | B | Very good |
| 60–69 | C | Good |
| 50–59 | D | Pass |
| 0–49 | F | Fail |

## 4. DATA STRUCTURES

The application uses a list of dictionaries.

A list stores multiple student records, while a dictionary stores the information of an individual student.

Example:

    students = [
        {
            "student_number": "2026001",
            "name": "Mary",
            "mark": 85,
            "grade": "A",
            "decision": "Excellent"
        }
    ]

## 5. PYTHON CONCEPTS USED

- Lists: Store multiple student records.
- Dictionaries: Store individual student information.
- While loop: Repeats the menu.
- For loop: Displays and processes student records.
- If/elif/else: Assigns grades.
- Try/except: Handles invalid numeric input.
- Append(): Adds student records.
- Break: Exits a loop.

## 6. HOW TO RUN THE PROGRAM

1. Install Python 3.
2. Open the project folder.
3. Open the terminal.
4. Run the following command:

    python grading_system.py

5. Select an option from the menu.

### APPLICATION MENU

1. Add student
2. Display all students
3. Class summary
4. Exit

## 7. CLASS STATISTICS

The program calculates:

- Total students.
- Class average.
- Highest mark.
- Lowest mark.
- Number of passes.
- Number of fails.

Average formula:

    Average = Total Marks / Total Students

The program checks whether student records exist before calculating statistics to prevent division by zero.

## 8. TESTING

| Test | Input | Expected result |
|---|---|---|
| T1 | 79 and 80 | B and A |
| T2 | 49 and 50 | F and D |
| T3 | -1, 101 and abc | Reject invalid marks |
| T4 | Empty class summary | Display informative message |
| T5 | Invalid menu option | Display warning |

Record the actual observed results after running each test.

## 9. GIT VERSION CONTROL

Initialise Git:

    git init

First commit:

    git add .
    git commit -m "Initial project setup"

Second commit:

    git add .
    git commit -m "Add grading rules and validation"

Third commit:

    git add .
    git commit -m "Add class statistics and testing"

View commit history:

    git log --oneline

## 10. REFLECTION

### Question 1
Why does the order of if/elif conditions matter at grade boundaries?

**Answer:** Python checks conditions from top to bottom. Correct ordering ensures that each student receives the correct grade.

### Question 2
What error could arise when calculating the average of an empty list?

**Answer:** A ZeroDivisionError may occur because the program would divide by zero students.

### Question 3
How would you adapt the program to handle two courses per student?

**Answer:** I would add two course mark fields to each student's dictionary and calculate separate grades and averages for each course.

## 11. CONCLUSION

The Student Grading System demonstrates the practical application of Python programming concepts, including lists, dictionaries, loops, conditional statements and input validation.

It provides an effective way of recording student marks, assigning grades and generating class performance statistics.

## 12. SUBMISSION REQUIREMENTS

- grading_system.py
- README.md
- Screenshots of successful program execution.
- Git commit history.
- Evidence of the five required tests.
-
