"""Example file"""


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print('The first 10 fib numbers are:')
for i in range(10):
    fib_num = fib(i)
    print(fib_num)
