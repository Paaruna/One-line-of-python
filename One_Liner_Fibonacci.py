# THE ONE-LINER
fib = lambda x: x if x<=1 else fib(x-1) + fib(x-2)
# THE RESULT
for i in range(int(input("enter the number"))):
   print(fib(i))
