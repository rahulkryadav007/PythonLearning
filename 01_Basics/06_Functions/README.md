# 06 — Functions

## Function kya hai?

**Professional Definition:** A function is a reusable block of code designed to perform a specific task.

**Hinglish:** Function ko ek reusable machine samjho. Ek baar logic likho aur jab zarurat ho function ko call karke use karo.

## Syntax

```python
def function_name():
    # code
```

## Basic Example

```python
def greet():
    print("Hello, Python!")

greet()
```

## Function with Parameter

```python
def greet(name):
    print("Hello", name)

greet("Rahul")
greet("Amit")
```

Parameter function ko input dene ka way hai.

## return

`return` function se result caller ko wapas bhejta hai.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

## Default Parameter

```python
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Rahul")
```

## Intermediate Example

```python
def calculate_total(price, quantity, discount=0):
    total = price * quantity
    discount_amount = total * discount / 100
    return total - discount_amount

bill = calculate_total(500, 3, 10)
print("Final Bill:", bill)
```

## Function kyun use karte hain?

- Code reuse hota hai.
- Code readable hota hai.
- Large problem ko small functions mein break kar sakte hain.
- Maintenance easy hota hai.
- Testing easier hoti hai.

## Common Mistakes

- `def` ke baad function name/parentheses miss karna.
- Function define karke call karna bhool jana.
- `return` aur `print` ka difference na samajhna.
- Indentation galat karna.

## Practice

1. `greet()` function banao.
2. Do numbers add karne ka function banao.
3. Even/odd check karne ka function banao.
4. Student average calculate karne ka function banao.
5. Simple calculator ke liye separate functions banao.

## Mini Challenge

Ek `calculate_result(marks1, marks2, marks3)` function banao jo total, average aur pass/fail status return kare.

## Summary

Function reusable code block hai. `def` se function define hota hai, parameters input le sakte hain aur `return` result wapas bhej sakta hai.

### Next Module
➡️ **02 — Data Structures**
