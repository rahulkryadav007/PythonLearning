# 02 — Variables & Data Types

## 1. Variable kya hai?

**Professional Definition:** A variable is a name used to reference a value/object in a Python program.

**Hinglish:** Variable ko ek labelled box samjho. Box ka naam variable hai aur uske andar jo value hai woh data hai.

```python
name = "Rahul"
age = 24
```

Yahan `name` aur `age` variables hain.

## 2. Variables kyun chahiye?

Agar hume data ko baar-baar use karna hai, to variable mein store/reference karke easily reuse kar sakte hain.

```python
price = 500
quantity = 3

total = price * quantity
print(total)
```

Output:

```text
1500
```

## 3. Python ke Common Data Types

| Data Type | Example | Meaning |
|---|---|---|
| `int` | `25` | Whole number |
| `float` | `25.5` | Decimal number |
| `str` | `"Rahul"` | Text |
| `bool` | `True` | True/False |
| `None` | `None` | No value |
| `list` | `[10, 20]` | Ordered mutable collection |
| `tuple` | `(10, 20)` | Ordered immutable collection |
| `set` | `{10, 20}` | Unique values |
| `dict` | `{ "name": "Rahul" }` | Key-value data |

## 4. Basic Example

```python
# Student ka naam store kar rahe hain
name = "Rahul"

# Student ki age store kar rahe hain
age = 24

# Student ke marks decimal value mein store kar rahe hain
marks = 85.5

# Student pass hai ya nahi, ye Boolean value store kar rahe hain
is_passed = True

print(name)
print(age)
print(marks)
print(is_passed)
```

## 5. type() Function

`type()` batata hai ki kisi value ka data type kya hai.

```python
age = 24
marks = 85.5
name = "Rahul"
is_passed = True

print(type(age))
print(type(marks))
print(type(name))
print(type(is_passed))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## 6. Type Conversion

Ek data type ko doosre compatible data type mein convert karna type conversion kehlata hai.

```python
# String number ko integer mein convert kar rahe hain
age = int("24")

# Integer ko float mein convert kar rahe hain
price = float(100)

print(age)
print(price)
```

## 7. Multiple Variables

```python
# Ek hi line mein multiple variables assign kar rahe hain
name, age, city = "Rahul", 24, "Dhanbad"

print(name)
print(age)
print(city)
```

## 8. Intermediate Example

```python
# Product ki price aur quantity store kar rahe hain
price = 499
quantity = 4

# Total amount calculate kar rahe hain
total = price * quantity

# Discount percentage store kar rahe hain
discount = 10

# Discount amount calculate kar rahe hain
discount_amount = total * discount / 100

# Final amount calculate kar rahe hain
final_amount = total - discount_amount

print("Total:", total)
print("Discount:", discount_amount)
print("Final Amount:", final_amount)
```

Output:

```text
Total: 1996
Discount: 199.6
Final Amount: 1796.4
```

## 9. Important Naming Rules

- Variable name number se start nahi ho sakta.
- Spaces allowed nahi hain.
- Python case-sensitive hai.
- Keywords ko variable name nahi banana chahiye.
- Meaningful names use karo.

Good:

```python
student_name = "Rahul"
total_marks = 450
```

Bad:

```python
x = "Rahul"
a = 450
```

## 10. Common Mistakes

❌ `2name = "Rahul"`

✅ `name2 = "Rahul"`

❌ `student name = "Rahul"`

✅ `student_name = "Rahul"`

❌ `Age = 24` aur baad mein `age` ko same variable samajhna.

Python mein `Age` aur `age` different names hain.

## 11. Interview Questions

**Q1. Python mein variable declare kaise karte hain?**

Python mein separate declaration required nahi hota. Assignment ke time variable create/reference ho jata hai.

**Q2. `type()` kya karta hai?**

`type()` kisi object/value ka type return karta hai.

**Q3. Python dynamically typed language ka kya meaning hai?**

Variable ka type explicitly declare karna required nahi hota; runtime par value/object ka type determine hota hai.

## 12. Practice

1. Apna name, age aur city variables mein store karo.
2. Do numbers store karke sum, difference aur product nikalo.
3. String ko integer mein convert karo.
4. Ek shopping bill calculate karo.
5. `type()` se 5 different values ke types check karo.

## 13. Mini Challenge

Ek student ke `name`, `marks1`, `marks2`, `marks3` variables banao. Total aur average calculate karke formatted output print karo.

## 14. Summary

- Variable data ko reference/store karne ke liye name provide karta hai.
- Python dynamically typed hai.
- Common types: `int`, `float`, `str`, `bool`, `None`, `list`, `tuple`, `set`, `dict`.
- `type()` type check karta hai.
- `int()`, `float()`, `str()` jaise functions type conversion mein help karte hain.

### Next Topic
➡️ **03 — Operators**
