# Python Big O Complexity

Python script using pyplot (Matlab-like) lib to demonstrate big-o complexities of standard algorithms.
Big O notation is used to classify algorithms based on their time and space complexity.


## Requirements
- matplotlib
- pyqt5 (lib GUI)

```sh
pip install matplotlib
pip install pyqt5
```

![Big O Chart](chart.png "Big O Chart")

## Common types of time complexities in Big O Notation

First, we will initialize some numbers list to help to explain the different types of algorithms in Big O Notation.

```python
numbersList = [1, 2, 3, 4, 5]
```

### 1. Constant O(1)
 In this type, the execution time is independent of the size of the input and will always take the same amount of time to execute.

```python
def constant(n):
  print(n[0])

constant(numbersList) # Output: 1
```


### 2. Linear O(n)
This type of algorithm will have a linear time complexity and will run linearly with the input size.

```python
def linear(n):
  for i in n:
    print(i) # Output: 1

linear(numbersList)

# Output:
# 1
# 2
# 3
# 4
# 5
```

### 3. Quadratic - O(n<sup>2</sup>) - polynomial
An algorithm has quadratic time complexity if the time to execute it is proportional to the square of the input size. In a few words, think of Linear but squared

```python
def quadratic(n):
  for i in n:
    for j in n:
      print(i, j)
    print('---')

quadratic(numbersList)

# Output:
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# ---
# 2 1
# 2 2
# 2 3
# 2 4
# 2 5
# ---
# 3 1
# 3 2
# 3 3
# 3 4
# 3 5
# ---
# 4 1
# 4 2
# 4 3
# 4 4
# 4 5
# ---
# 5 1
# 5 2
# 5 3
# 5 4
# 5 5
# ---
```
