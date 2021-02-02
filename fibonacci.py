import sys


def fib(n):
    # Recursive
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # while n >= 0:
    #     return fib(n - 1) + fib(n - 2)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    print(fib(int(sys.argv[1])))