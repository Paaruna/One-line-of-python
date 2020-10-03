from functools import reduce

# THE ONE-LINER
factorial = reduce(lambda x, y: x * y, range(1, int(input("enter the number"))+1))

# THE RESULT
print(factorial)
