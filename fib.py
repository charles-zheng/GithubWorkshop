"""Example file"""


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


how_many_numbers = input('Enter how many fib numbers you want to see: ')
print('The first ' + how_many_numbers + ' fib numbers are:')
for i in range(int(how_many_numbers)):
    fib_num = fib(i)
    print(fib_num)
