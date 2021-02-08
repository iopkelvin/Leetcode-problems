def uniqueMorseRepresentations(words):
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
     "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    # seen = {''.join(morse[ord(c)-ord('a')] for c in word) for word in words}
    # print(seen)
    print(ord('g') - ord('a'))
    return



if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    print(uniqueMorseRepresentations(words))
