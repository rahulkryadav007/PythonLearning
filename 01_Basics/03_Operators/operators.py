# ============================================================
# OPERATORS — BASIC TO INTERMEDIATE
# ============================================================

# -------------------- Arithmetic -----------------------------
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# -------------------- Comparison -----------------------------
# Comparison operators ka result True ya False hota hai.
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)

# -------------------- Logical -------------------------------
age = 22
has_id = True

# Dono conditions True honi chahiye.
print("Can enter:", age >= 18 and has_id)

# At least ek condition True honi chahiye.
print("Special access:", age >= 60 or has_id)

# True ko False aur False ko True karta hai.
print("Without ID:", not has_id)

# -------------------- Assignment ----------------------------
score = 10
score += 5   # score = score + 5
score *= 2   # score = score * 2
print("Final Score:", score)

# -------------------- Membership ----------------------------
skills = ["Python", "Java", "SQL"]
print("Python" in skills)
print("C++" not in skills)

# -------------------- Intermediate Example ------------------
marks = 78
attendance = 85

# Student ko pass hone ke liye marks aur attendance dono required hain.
is_eligible = marks >= 40 and attendance >= 75

print("Eligible:", is_eligible)
