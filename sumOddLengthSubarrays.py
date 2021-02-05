def sumOddLengthSubarrays(A):
    n = len(A)
    for i in range(1, n+1, 2):
        print('i ', i)
        for j in range(n - i + 1):
            print(' j ', j)
            print('   ', A[j:j + i], sum(A[j:j + i]))
    return


if __name__ == '__main__':
    A = [1,4,2,5,3]
    print(sumOddLengthSubarrays(A))