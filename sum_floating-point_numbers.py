# I did not pass this algorithm for a DE position.
def sum_floating_nums(a, b):
    """
    Sum two large floating-point numbers without turning string into integers
    params:
        a = string
        b = string
    return: Sum of two strings (floats)
    """
    # Split strings by the decimal point. Strings will be held inside list.
    split_a = a.split('.')
    split_b = b.split('.')
    # Invert digits from back to front for both integers and fractions
    int_a, frac_a = [], []
    int_b, frac_b = [], []
    for i in split_a[0][::-1]:
        int_a.append(i)
    for i in split_a[1][::-1]:
        frac_a.append(i)
    for i in split_b[0][::-1]:
        int_b.append(i)
    for i in split_b[1][::-1]:
        frac_b.append(i)
    # Pad with zeros to make equal length for fractions and integers
    # Pad front (integer)
    n_a = len(int_a)
    n_b = len(int_b)
    diff_n = abs(n_a - n_b)
    if n_a < n_b:
        int_a += '0' * diff_n
    else:
        int_b += '0' * diff_n
    # Pad back (decimals)
    m_a = len(frac_a)
    m_b = len(frac_b)
    diff_m = abs(m_a - m_b)
    if m_a < m_b:
        for i in range(diff_m):
            frac_a.insert(0, '0')
    else:
        for i in range(diff_m):
            frac_b.insert(0, '0')
    # Do addition for both fractions and integers keeping account of carry
    # Add fraction
    len_frac_a = len(frac_a)
    len_frac_b = len(frac_b)
    i = 0
    carry = 0
    while i < len_frac_a and i < len_frac_b:
        sum = eval(frac_a[i] + '+' + frac_b[i]) + carry
        frac_a[i] = sum % 10
        carry = sum / 10
        i += 1
    # Last carry before decimal point is still being held
    # Add integer
    len_int_a = len(int_a)
    len_int_b = len(int_b)
    i = 0
    while i < len_int_a and i < len_int_b:
        sum = eval(int_a[i] + '+' + int_b[i]) + carry
        int_a[i] = sum % 10
        carry = sum / 10
        i += 1

    if carry != 0:
        int_a.append(carry)
    # Get result by inverting list again, and appending decimal point after decimals.
    result = ''
    for i in int_a[::-1]:
        result += str(i)
    result += '.'
    for i in frac_a[::-1]:
        result += str(i)

    print(result)
    return


if __name__ == '__main__':
    print('First number as string:')
    a = input()
    print('Second number as string:')
    b = input()
    sum_floating_nums(a, b)