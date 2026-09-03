# 05 — Loops

## Loop kya hai?

**Professional Definition:** A loop repeatedly executes a block of code while iterating over a sequence or while a condition remains true.

**Hinglish:** Agar same kaam baar-baar karna hai, to same code baar-baar likhne ke bajay loop use karte hain.

## for Loop

Sequence ke items par iterate karne ke liye useful hai.

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

## while Loop

Jab tak condition True hai, loop chalta rahega.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## break

Loop ko immediately stop karta hai.

```python
for number in range(1, 11):
    if number == 6:
        break
    print(number)
```

## continue

Current iteration skip karke next iteration par chala jata hai.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

## Nested Loop

Ek loop ke andar doosra loop.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row, column)
```

## Intermediate Example

```python
# 1 se 20 tak sirf even numbers print kar rahe hain.
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
```

## Common Mistakes

- `while` loop mein update bhoolne se infinite loop ho sakta hai.
- `range()` ka stop value generally include nahi hota.
- Indentation maintain karna zaroori hai.

## Practice

1. 1 se 10 print karo.
2. 1 se 100 tak even numbers print karo.
3. 1 se 100 tak sum calculate karo.
4. Multiplication table banao.
5. Number guessing logic practice karo.

### Next Topic
➡️ **06 — Functions**
