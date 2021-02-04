def sumZero(n):
    # a = range(1, n)
    # return a + [-sum(a)]
    print(range(1 - n, n, 2))

if __name__ == '__main__':
    n = 5
    print(sumZero(n))