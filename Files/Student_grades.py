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