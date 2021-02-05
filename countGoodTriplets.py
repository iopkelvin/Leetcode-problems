def countGoodTriplets(arr, a, b, c):
    size = len(arr)
    count = 0
    for i in range(size - 2):
        print('i ', i)
        for j in range(i+1, size-1):
            print(' j ', j)
            for k in range(j+1, size):
                print('  k ', k)
    return


if __name__ == '__main__':
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    print(countGoodTriplets(arr, a, b, c))