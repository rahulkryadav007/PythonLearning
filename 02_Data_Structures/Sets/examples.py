# ============================================================
# SETS — BASIC TO INTERMEDIATE
# ============================================================

# Set duplicate values ko automatically remove karta hai.
numbers = {10, 20, 30, 10, 20}
print("Unique numbers:", numbers)

# New value add kar rahe hain.
numbers.add(40)
print(numbers)

# Do groups ke common aur combined elements find kar rahe hain.
python_students = {"Rahul", "Amit", "Neha"}
java_students = {"Amit", "Ravi", "Neha"}

print("All students:", python_students | java_students)
print("Common students:", python_students & java_students)
print("Only Python students:", python_students - java_students)
