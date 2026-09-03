# ============================================================
# CONDITIONAL STATEMENTS — BASIC TO INTERMEDIATE
# ============================================================

# User ki age ke basis par decision le rahe hain.
age = 20

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# Marks ke basis par grade decide kar rahe hain.
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

# Multiple conditions ko logical operator ke saath use kar sakte hain.
attendance = 85

if marks >= 40 and attendance >= 75:
    print("Student is eligible")
else:
    print("Student is not eligible")
