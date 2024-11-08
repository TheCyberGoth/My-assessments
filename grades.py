mark = int(input("Please provide student's mark: "))

if 70 <= mark <= 100:
    grade = "A"
elif 60 <= mark <= 69:
    grade = "B"
elif 50 <= mark <= 59:
    grade = "C"
elif 40 <= mark <= 49:
    grade = "D"
elif 30 <= mark <= 39:
    grade = "E"
elif 20 <= mark <= 29:
    grade = "F"
else:
    grade = "Invalid mark!"                 


print("Student grade is: ", grade)