# 04 — Conditional Statements

## Conditional statement kya hai?

**Professional Definition:** Conditional statements control program flow by executing different code based on whether a condition is true or false.

**Hinglish:** Program ko decision lena ho — jaise age 18 ya usse zyada hai to vote allowed, warna not allowed — tab conditions use karte hain.

## Syntax

```python
if condition:
    # condition True hone par code
elif another_condition:
    # second condition True hone par code
else:
    # koi condition True na ho to code
```

## Basic Example

```python
age = 20

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

## Multiple Conditions

```python
marks = 82

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Need improvement")
```

## Nested if

```python
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Bring your ID")
else:
    print("Entry not allowed")
```

## Intermediate Example

```python
username = "admin"
password = "python123"

# Pehle username check kar rahe hain, phir password.
if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")
```

## Common Mistakes

- `if` ke baad colon `:` bhoolna.
- Indentation galat karna.
- `=` ko comparison samajhna; comparison ke liye `==` use hota hai.

## Practice

1. Positive/negative number check karo.
2. Even/odd check karo.
3. Student grade calculator banao.
4. Voting eligibility check karo.
5. Login validation program banao.

### Next Topic
➡️ **05 — Loops**
