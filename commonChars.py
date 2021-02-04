import collections
def commonChars(A):
    res = collections.Counter(A[0])
    print(res)
    for a in A:
        res &= collections.Counter(a)
    return list(res.keys())


if __name__ == '__main__':
    A = ["bella","label","roller", 'role']
    print(commonChars(A))