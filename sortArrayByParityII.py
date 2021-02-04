def sortArrayByParityII(n):
    # pairs = []
    # odds = []
    # for i, j in enumerate(n):
    #     if j % 2 == 0:
    #         pairs.append(j)
    #     else:
    #         odds.append(j)
    # result = []
    # for i, j in zip(pairs, odds):
    #     result.append(i)
    #     result.append(j)
    # return result
    i = 0
    j = 1
    sz = len(n)
    while i < sz and j < sz:
        print('i ', n[i], 'j ', n[j])
        if n[i] % 2 == 0:
            print('if')
            i += 2
            print(i)
        elif n[j] % 2 == 1:
            print('elif')
            j += 2
            print(j)
        else:
            print('else')
            n[i], n[j] = n[j], n[i]
            print(n[i], n[j])
            i += 2
            j += 2
    return n



if __name__ == "__main__":
    n = [4,2,5,7]
    print(sortArrayByParityII(n))