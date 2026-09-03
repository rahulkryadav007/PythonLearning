# Sets in Python

## Set kya hai?

Set ek unordered collection hai jisme unique elements store hote hain.

**Hinglish:** Set ko unique-items wala box samjho. Same value multiple baar add karoge to set duplicate ko retain nahi karega.

## Basic Example

```python
numbers = {10, 20, 30, 10}
print(numbers)
```

Output mein `10` ek hi baar rahega.

## Add and Remove

```python
skills = {"Python", "Java"}

skills.add("SQL")
skills.remove("Java")

print(skills)
```

## Set Operations

```python
python_students = {"Rahul", "Amit", "Neha"}
java_students = {"Amit", "Ravi", "Neha"}

print(python_students | java_students)  # union
print(python_students & java_students)  # intersection
print(python_students - java_students)  # difference
```

## Important Points

- Unique values.
- Duplicate values automatically remove ho jaati hain.
- Traditional indexing/slicing supported nahi hai.
- Set operations very useful hain.

## Practice

1. Duplicate numbers ki list ko set mein convert karo.
2. Do students groups ka common data find karo.
3. Union aur difference practice karo.

### Next
➡️ **Dictionaries**
