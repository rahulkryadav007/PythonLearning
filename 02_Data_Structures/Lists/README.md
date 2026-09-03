# Lists in Python

## List kya hai?

List ek ordered aur mutable collection hai jisme multiple values store kar sakte hain.

**Hinglish:** List ko shopping bag samjho jisme multiple items rakh sakte ho, aur baad mein item add/remove/change bhi kar sakte ho.

## Basic Example

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
```

## Indexing

Python mein indexing `0` se start hoti hai.

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])
print(fruits[1])
```

## Modify List

```python
fruits = ["Apple", "Banana", "Mango"]

# Existing item ko change kar rahe hain
fruits[1] = "Orange"

# New item add kar rahe hain
fruits.append("Grapes")

print(fruits)
```

## Common Methods

```python
numbers = [10, 20, 30]

numbers.append(40)       # End mein item add
numbers.insert(1, 15)    # Specific index par add
numbers.remove(20)       # Value remove
last = numbers.pop()     # Last item remove karke return

print(numbers)
print("Removed:", last)
```

## Slicing

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
```

## Loop Through List

```python
skills = ["Python", "Java", "SQL"]

for skill in skills:
    print("Skill:", skill)
```

## Intermediate Example

```python
marks = [78, 85, 91, 66, 73]

# Total aur average calculate kar rahe hain.
total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", average)
```

## Important Points

- Ordered hoti hai.
- Mutable hoti hai.
- Duplicate values allowed hain.
- Indexing aur slicing supported hai.

## Practice

1. Apne 5 favourite fruits ki list banao.
2. List mein item add/remove/change karo.
3. List ke maximum aur minimum marks find karo.
4. List ke saare even numbers print karo.
5. Student marks ka average calculate karo.

### Next
➡️ **Tuples**
