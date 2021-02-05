def generateTheString(n):
    print('ab'[n & 1] * (n-1))
    return 'b' + 'ab'[n & 1] * (n -1)


if __name__ == '__main__':
    n = 3
    print(generateTheString(n))