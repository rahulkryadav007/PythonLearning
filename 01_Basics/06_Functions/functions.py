# ============================================================
# FUNCTIONS — BASIC TO INTERMEDIATE
# ============================================================

# Simple reusable function define kar rahe hain.
def greet():
    print("Hello, Python learner!")

# Function ko call kar rahe hain.
greet()

# Parameter ke through function ko data pass kar rahe hain.
def greet_user(name):
    print("Hello", name)

greet_user("Rahul")
greet_user("Amit")

# return function ka result caller ko wapas deta hai.
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# Default value tab use hoti hai jab argument pass na kiya jaye.
def welcome(name="Student"):
    print("Welcome", name)

welcome()
welcome("Rahul")

# Intermediate: reusable bill calculation function.
def calculate_total(price, quantity, discount=0):
    total = price * quantity
    discount_amount = total * discount / 100
    final_amount = total - discount_amount
    return final_amount

bill = calculate_total(500, 3, 10)
print("Final Bill:", bill)
