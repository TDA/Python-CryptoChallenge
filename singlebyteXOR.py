__author__ = 'saipc'

import string
from fixedXOR import fixedXOR

def singleByteXOR(a):
    a_bytearray = bytearray(a.decode('hex'))
    letters = [x for x in string.ascii_letters]
    for key in letters:
        # or can reuse the old pgm, much more pythonic :)
        new_key2 = key * len(a_bytearray)
        print fixedXOR(a, new_key2.encode('hex')).decode('hex')




if __name__ == '__main__':
    xor = singleByteXOR('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

