# Dictionaries in Python

## Dictionary kya hai?

Dictionary ek mutable collection hai jo data ko **key-value pairs** mein store karta hai.

**Hinglish:** Dictionary ko real-life dictionary ya student record samjho: ek key ke through uski related value access karte hain.

```python
student = {
    "name": "Rahul",
    "age": 24,
    "branch": "CSE"
}
```

## Access Value

```python
print(student["name"])
print(student["age"])
```

## Add and Update

```python
student["city"] = "Dhanbad"   # New key-value add
student["age"] = 25           # Existing value update
```

## Remove

```python
student.pop("city")
```

## Loop Through Dictionary

```python
student = {"name": "Rahul", "age": 24, "branch": "CSE"}

for key, value in student.items():
    print(key, ":", value)
```

## Intermediate Example

```python
students = {
    "101": {"name": "Rahul", "marks": 85},
    "102": {"name": "Amit", "marks": 91}
}

print(students["101"]["name"])
print(students["102"]["marks"])
```

Ye nested dictionary ka example hai, jo real applications mein structured data represent karne ke liye useful hota hai.

## Important Points

- Data key-value pair mein hota hai.
- Keys unique honi chahiye.
- Dictionary mutable hai.
- `.keys()`, `.values()`, `.items()` commonly used methods hain.

## Common Mistake

List mein index use hota hai, dictionary mein normally key use hoti hai.

```python
student["name"]  # correct
```

## Practice

1. Apni profile dictionary banao.
2. New key add karo.
3. Existing value update karo.
4. Dictionary par loop chalao.
5. Nested student records banao.

### Next Module
➡️ **Advanced Python Concepts**
