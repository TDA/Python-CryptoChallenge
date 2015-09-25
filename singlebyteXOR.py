__author__ = 'saipc'

import string
from fixedXOR import fixedXOR

def singleByteXOR(a):
    # decode from hex
    a_decoded = a.decode('hex')
    # convert to bytes
    a_bytearray = bytearray(a_decoded)
    letters = [x for x in string.ascii_letters]
    c_bytearray = bytearray(len(a_bytearray))
    for key in letters:
        new_key = int(ord(key))
        for x in xrange(0, len(a_bytearray)):
            c_bytearray[x] = a_bytearray[x] ^ new_key
        #print c_bytearray, chr(new_key)

        # or can reuse the old pgm
        new_key2 = key * len(a_bytearray)
        print fixedXOR(a, new_key2.encode('hex')).decode('hex')




if __name__ == '__main__':
    xor = singleByteXOR('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

