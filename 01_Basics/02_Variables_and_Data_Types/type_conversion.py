# ============================================================
# TYPE CONVERSION
# ============================================================

# input() se age string ke form mein milti hai.
age_text = input("Enter your age: ")
print("Before conversion:", type(age_text))

# String ko integer mein convert kar rahe hain.
age = int(age_text)
print("After conversion:", type(age))

# Ab hum arithmetic operation kar sakte hain.
next_year_age = age + 1
print("Next year age:", next_year_age)

# Integer ko float mein convert karna.
number = 10
decimal_number = float(number)
print(decimal_number)

# Number ko string mein convert karna.
marks = 95
marks_text = str(marks)
print("Marks:", marks_text)
print("Type:", type(marks_text))
