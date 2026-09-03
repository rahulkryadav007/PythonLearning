# ============================================================
# TUPLES — BASIC TO INTERMEDIATE
# ============================================================

# Tuple ordered aur immutable collection hai.
student = ("Rahul", 24, "CSE")

print("Student:", student)
print("Name:", student[0])
print("Age:", student[1])

# Tuple unpacking se values ko separate variables mein le rahe hain.
name, age, branch = student

print(name)
print(age)
print(branch)

# Tuple duplicate values ko allow karta hai.
numbers = (10, 20, 10, 30)
print(numbers)
