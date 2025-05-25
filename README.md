# Assignment-2
Q. 1 Grade Checker
Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"

def grade_checker(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = int(input("Enter the Score : "))
print(f"The Grade is : {grade_checker(score)}")

 

Q. 2 Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.
Used dictionary and basic operations. Using if else:

def student_grades():
    grades = {}
    while True:
        action = input("Choose an action: add, update, print, or exit : ").strip().lower()
        if action == "add":
            name = input("Enter Student Name : ")
            grade = input("Enter Student Grade : ")
            grades[name] = grade
            print(f"Added {name} with grade {grade}.")
        elif action == "update":
            name = input("Enter Student Name to update : ")
            if name in grades:
                grade = input("Enter new Grade : ")
                grades[name] = grade
                print(f"Updated {name} grade to {grade}.")
            else:
                print("Student not found.")
        elif input == "print":
            for name, grade in grades.items():
                print(f"{name} : {grade}")
        elif action == "exit":
            break
        else:
            print("Invalid action. Please Choose Again")

student_grades()

 

Q. 3 Write to a File
Write a program to create a text file and write some content to it.
Using file functions like write and open.

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}.")

a = input("Enter File name : ")
b = input("Enter content : ")
write_to_file(a,b)

 

Q. 4 Read from File
We used open in read mode and file.read to read and print to display.

def read_from_file(filename):
    with open(filename,'r') as file:
        content = file.read()
    print(content)

a = input("Enter file name : ")
read_from_file(a)

 

