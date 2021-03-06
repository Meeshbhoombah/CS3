#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    
    # reverse digits so index corresponds with power
    digits = digits[::-1]
    
    # binary
    if set(digits) <= set("01"): 
        as_int = 0
        # use index as power
        for index, digit in enumerate(digits):
            if digit is "1":
                as_int += math.pow(base, index)

        return int(as_int)
    
    # hexadecimal
    if "0x" in digits:

        # get digits only 
        digits = digits[:-2]

        # use lowercase for check against string.hexdigits
        digits = digits.lower()

        as_int = 0
        for index, digit in enumerate(digits):
            try:
                int(digit)
                as_int += digit * math.pow(base, index) 
            except:
                as_int += string.hexdigits.index(digit) * math.pow(base, index)

        return int(as_int)

    # base 2 - 36
    as_int = 0
    for index, digit in enumerate(digits):
        as_int += string.hexdigits.index(digit) * math.pow(base, index) 

    return as_int

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    
    # limit hexdigits and make all upcase
    hexdigit_string = string.digits + string.ascii_lowercase

    # TODO: Encode number in binary (base 2)
    #
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    if number < base:
        return hexdigit_string[number]
    else:
        return encode(number // base, base) + hexdigit_string[number % base]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    digits = int(decode(digits, base1))
    return encode(digits, base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

