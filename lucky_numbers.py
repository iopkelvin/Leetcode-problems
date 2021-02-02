import sys


def lucky_numbers(array):
    '''
    Given a m * n matrix of distinct numbers, return all lucky numbers.
    A lucky number is an element of the matrix such that it is the min element in its row and max in its column.
    '''
    min_row = []
    max_col = []
    for i in array:
        min_row.append(min(i))
    for i in zip(*array):
        max_col.append(max(i))
    print(min_row)
    print(max_col)
    return set(min_row) & set(max_col)


if __name__ == '__main__':
    print(lucky_numbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))