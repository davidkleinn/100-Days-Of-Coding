student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}



for student, score in student_scores.items():
    
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    if 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    if 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    if score <= 70:
        student_grades[student] = "Fail"

print(student_grades)