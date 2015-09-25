__author__ = 'saipc'

import string

def singleByteXOR(a):
    # decode from hex
    a = a.decode('hex')
    # convert to bytes
    a_bytearray = bytearray(a)
    letters = [x for x in string.ascii_letters]
    numbers = [x for x in xrange(0,10)]
    for key in letters + numbers:
        print key


if __name__ == '__main__':
    xor = singleByteXOR('1c0111001f010100061a024b53535009181c')
    print xor
