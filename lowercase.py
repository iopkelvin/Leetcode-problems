import sys


def toLowerCase(string):
    """
    Turns string into lower case using ord
    :param string: A string
    :return: lower case of string
    """
    lowered_string = ""
    for i in string:
        if 65 <= ord(i) <= 90:
            lowered_string += chr(ord(i) + 32)
        else:
            lowered_string += i
    return lowered_string


if __name__ == '__main__':
    print(toLowerCase(sys.argv[1]))