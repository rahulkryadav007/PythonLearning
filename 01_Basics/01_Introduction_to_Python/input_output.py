# ============================================================
# INPUT AND OUTPUT
# ============================================================

# input() user se value lene ke liye use hota hai.
name = input("Enter your name: ")

# User se city ka naam le rahe hain.
city = input("Enter your city: ")

# User ki entered values ko display kar rahe hain.
print("Hello", name)
print("You are from", city)

# NOTE: input() se received value default mein string hoti hai.
age = input("Enter your age: ")
print("Your age is", age)
print("Type of age:", type(age))
