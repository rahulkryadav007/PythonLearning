# ============================================================
# DICTIONARIES — BASIC TO INTERMEDIATE
# ============================================================

# Student ki information ko key-value pairs mein store kar rahe hain.
student = {
    "name": "Rahul",
    "age": 24,
    "branch": "CSE"
}

# Key ke through value access kar rahe hain.
print("Name:", student["name"])
print("Age:", student["age"])

# New key-value pair add kar rahe hain.
student["city"] = "Dhanbad"

# Existing value update kar rahe hain.
student["age"] = 25

# Dictionary ke key-value pairs par loop chala rahe hain.
for key, value in student.items():
    print(key, ":", value)

# Intermediate: nested dictionary se structured student data store kar rahe hain.
students = {
    "101": {"name": "Rahul", "marks": 85},
    "102": {"name": "Amit", "marks": 91}
}

print("Student 101:", students["101"]["name"])
print("Student 102 marks:", students["102"]["marks"])
