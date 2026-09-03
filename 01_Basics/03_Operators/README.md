# 03 — Operators

## Operators kya hote hain?

**Professional Definition:** Operators are symbols or keywords used to perform operations on values and expressions.

**Hinglish:** Operator ek special symbol/keyword hai jo data ke saath koi operation perform karta hai.

Example:

```python
10 + 5
```

Yahan `+` addition operator hai.

## Types of Operators

- Arithmetic
- Comparison
- Logical
- Assignment
- Membership
- Identity

## 1. Arithmetic Operators

`+`, `-`, `*`, `/`, `//`, `%`, `**`

```python
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Remainder
print(a ** b)  # Power
```

## 2. Comparison Operators

Comparison ka result normally `True` ya `False` hota hai.

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

## 3. Logical Operators

`and`, `or`, `not` multiple conditions ke saath kaam karte hain.

```python
age = 22
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

## 4. Assignment Operators

```python
score = 10
score += 5
score *= 2

print(score)
```

## 5. Membership Operators

`in` aur `not in` check karte hain ki koi value collection ke andar present hai ya nahi.

```python
skills = ["Python", "Java", "SQL"]

print("Python" in skills)
print("C++" not in skills)
```

## 6. Identity Operators

`is` aur `is not` object identity check karte hain. `==` values compare karta hai; `is` identity.

```python
a = None
b = None

print(a is b)
print(a is not b)
```

## Intermediate Example

```python
marks = 78
attendance = 85

# Student tab eligible hai jab marks aur attendance dono required limit se upar hon.
eligible = marks >= 40 and attendance >= 75

print("Eligible:", eligible)
```

## Common Mistake

`=` assignment ke liye hai, jabki `==` comparison ke liye.

```python
age = 20      # assignment
print(age == 20)  # comparison
```

## Practice

1. Do numbers ke saath saare arithmetic operators try karo.
2. Do numbers compare karo.
3. `and`, `or`, `not` ke examples banao.
4. List mein kisi item ki membership check karo.
5. Ek student eligibility program banao.

## Summary

Operators Python programs mein calculations, comparisons, conditions aur object/value checks perform karne ke liye use hote hain.

### Next Topic
➡️ **04 — Conditional Statements**
