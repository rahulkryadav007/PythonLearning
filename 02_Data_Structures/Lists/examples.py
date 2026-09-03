# ============================================================
# LISTS — BASIC TO INTERMEDIATE
# ============================================================

# Multiple values ko ek ordered collection mein store kar rahe hain.
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# Index 0 se start hota hai.
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Existing item ko modify kar rahe hain.
fruits[1] = "Orange"

# End mein new item add kar rahe hain.
fruits.append("Grapes")

print("Updated fruits:", fruits)

# List ke har item par loop chala rahe hain.
for fruit in fruits:
    print("Fruit:", fruit)

# Intermediate: marks ka total aur average.
marks = [78, 85, 91, 66, 73]
total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
