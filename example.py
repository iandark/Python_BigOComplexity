
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
    print("---")


# constant(numbersList)
# print()
# linear(numbersList)
# quadratic(numbersList)


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(numbers_list, item):
    first = 0
    last = len(numbers_list)-1
    found = False
    step = 1

    print("Looking for number " + str(item) + ".")
    while first <= last and not found:
        midpoint = (first + last)//2

        if numbers_list[midpoint] == item:
            found = True
            if step == 1:
                print(str(step) + ". Found item in the middle of list. Position " +
                  str(midpoint)+ ".")
            else:
                print(str(step) + ". Found item in position " +
                      str(midpoint) + ".")

            step += 1
        else:
            if step == 1:
                print(str(step) + ". Number not found in the middle of list in position " + str(midpoint) + ".")

            if item < numbers_list[midpoint]:
                last = midpoint-1
                print(str(step) + ". The number we're looking for is lower than the number " +
                      str(numbers_list[midpoint]) + " in position " + str(midpoint) + ".")
                print("   Ignoring the left-hand side because these numbers are greater than the number we're looking for.")
                step += 1
            else:
                first = midpoint+1
                if step > 2:
                    print(str(step) + ". Number not found in position " + str(midpoint) +
                          " trying position " + str(midpoint+1))
                    print(
                    "   Ignoring the left-hand side because these numbers are greater than the number we're looking for.")

                step += 1

    return found


print(binary_search(items, 6))
