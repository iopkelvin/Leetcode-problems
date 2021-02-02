def maxDepth(s):
    result = counter = 0
    for i in s:
        print('i is ', i)
        if i == '(':
            counter += 1
            result = max(result, counter)

        if i == ')':
            counter -= 1
        print('counter ', counter)
        print('result ', result)
    return result


if __name__ == '__main__':
    s = "(1+(2*3)+((8)/4))+1"
    maxDepth(s)