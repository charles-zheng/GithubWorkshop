"""Example file"""


def fib(n):
    f0, f1 = 0, 1
    for _ in range(n):
        f0, f1 = f1, f0 + f1
    return f0


print('The first 10 fib numbers are:')
for i in range(10):
    fib_num = fib(i)
    print(fib_num)
