# ============================================================
# LOOPS — BASIC TO INTERMEDIATE
# ============================================================

# for loop range ke numbers par iterate kar raha hai.
for number in range(1, 6):
    print(number)

# List ke har item ko one-by-one access kar rahe hain.
skills = ["Python", "Java", "SQL"]

for skill in skills:
    print("Skill:", skill)

# while loop tab tak chalega jab tak condition True hai.
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

# break loop ko condition match hote hi stop kar deta hai.
for number in range(1, 11):
    if number == 6:
        break
    print("Break example:", number)

# continue current iteration ko skip karta hai.
for number in range(1, 6):
    if number == 3:
        continue
    print("Continue example:", number)

# Intermediate: 1 se 20 tak even numbers print kar rahe hain.
for number in range(1, 21):
    if number % 2 == 0:
        print("Even:", number)
