
numbersList = [1, 2, 3, 4, 5]

# Constant
def constant(n):
  print(n[0])

# Linear
def linear(n):
  for i in n:
    print(i)

# Quadratic
def quadratic(n):
  for i in n:
    for j in n:
      print(i, j)
    print('---')


constant(numbersList)
print()
linear(numbersList)
quadratic(numbersList)
