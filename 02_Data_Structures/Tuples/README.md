# Tuples in Python

## Tuple kya hai?

Tuple ek ordered aur immutable collection hai.

**Hinglish:** Tuple list jaisa hota hai, lekin tuple banne ke baad uske existing elements ko directly change nahi kar sakte.

```python
coordinates = (10, 20)
print(coordinates[0])
```

## Basic Example

```python
student = ("Rahul", 24, "Python")
print(student)
```

## Indexing

```python
colors = ("Red", "Green", "Blue")
print(colors[0])
print(colors[-1])
```

## Tuple Unpacking

```python
student = ("Rahul", 24, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)
```

## Important Points

- Ordered hai.
- Immutable hai.
- Duplicate values allowed hain.
- Indexing/slicing supported hai.
- Fixed/unchanging data ke liye useful hai.

## Common Mistake

```python
coordinates = (10, 20)
# coordinates[0] = 100  # TypeError
```

## Practice

1. Ek tuple mein apni basic information store karo.
2. Tuple indexing practice karo.
3. Tuple unpacking karo.
4. Tuple mein duplicate values ka behaviour observe karo.

### Next
➡️ **Sets**
