def flipAndInvertImage(A):
    res = []
    print(A)
    for i in A:
        i[:] = i[::-1]
        print(i)
        res.append(list(map(lambda x: 0 if x == 1 else 1, i)))
    print(res)


if __name__ == '__main__':
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(flipAndInvertImage(A))
