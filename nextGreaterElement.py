def next_greater(arr1, arr2):
    d = {}
    st = []
    output = []
    for num in arr2:
        print('number:', num)
        while len(st) and st[-1] < num:
            d[st.pop()] = num
        print(d)
        st.append(num)
        print('st: ', st)
    for num1 in arr1:
        output.append(d.get(num1, -1))
    print(output)
    return

if __name__ == '__main__':
    arr1 = [4, 1, 2, 5]
    arr2 = [1, 3, 2, 4, 5]
    next_greater(arr1, arr2)