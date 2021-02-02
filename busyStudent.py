def busyStudent(start, end, query):
    i, j = 0, 0
    count = 0
    while len(start) > i and len(end) > j:
        if query in range(start[i], end[j] + 1):
            count += 1
        i += 1
        j += 1
    return count


if __name__ == "__main__":
    start = [4]
    end = [4]
    query = 4
    print(busyStudent(start, end, query))