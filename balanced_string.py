def balanced_string(s):
    counter = 0
    result = 0
    for i in s:
        counter += i == 'L'
        counter -= i == 'R'
        result += counter == 0
    print(result)
    return


if __name__ == '__main__':
    s = "RLRRLLRLRL"
    balanced_string(s)