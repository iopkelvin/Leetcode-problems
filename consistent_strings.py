def countConsistentStrings(allowed, list_str):
    counter = 0
    for word in list_str:
        if all(c in allowed for c in word):
            counter += 1
    print(counter)
    return counter


if __name__ == '__main__':
    allowed = "ab"
    list_str = ["ad","bd","aaab","baa","badab"]
    countConsistentStrings(allowed, list_str)