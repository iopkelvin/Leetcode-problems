def countNegatives(grid):
    i = len(grid) - 1
    j = 0
    count = 0
    while i >= 0 and j < len(grid[0]):
        print(i, j)
        if grid[i][j] < 0:
            count += len(grid[0]) - j
            i -= 1
            print('count ', count)
        else:
            j += 1
    return count


if __name__ == "__main__":
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    countNegatives(grid)

# def binary_search(row):
    #     start, end = 0, len(row)
    #     while start < end:
    #         mid = start + (end - start) // 2
    #         if row[mid] < 0:
    #             end = mid
    #         else:
    #             start = mid + 1
    #     return len(row) - start
    #
    # count = 0
    # for row in grid:
    #     count += bin(row)
    # return count