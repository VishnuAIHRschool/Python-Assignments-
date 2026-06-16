# Student Grade System
# 


# Student Grade System

student_name = input("Enter student name: ")

marks = int(input("Enter student marks: "))

if 90 <= marks <= 100:
    grade = "A"

elif 80 <= marks <= 89:
    grade = "B"

elif 70 <= marks <= 79:
    grade = "C"

elif 60 <= marks <= 69:
    grade = "D"

else:
    grade = "F"

print("\nStudent Name:", student_name)
print("Marks:", marks)
print("Grade:", grade)

if marks > 95:
    print("Very Good")