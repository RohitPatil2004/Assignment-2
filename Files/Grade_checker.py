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
