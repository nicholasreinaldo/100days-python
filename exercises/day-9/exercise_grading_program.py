student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.

student_grades = {}

# Write your code below to add the grades to student_grades.👇

for student_name in student_scores:
    student_grades[student_name] = ""
    if student_scores[student_name] > 90:
        student_grades[student_name] = "Outstanding"
    elif student_scores[student_name] > 80:
        student_grades[student_name] = "Exceeds Expectations"
    elif student_scores[student_name] > 70:
        student_grades[student_name] = "Acceptable"
    else:
        student_grades[student_name] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)