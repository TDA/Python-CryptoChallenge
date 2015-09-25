__author__ = 'saipc'

import string
from fixedXOR import fixedXOR


def calculateFrequency(str, key):
    freq_map = {x: 0 for x in "etaoinshrdlu"}
    for char in str:
        if freq_map.has_key(char):
            freq_map[char] = freq_map[char] + 1
    sum = 0
    for char in freq_map.keys():
        sum += freq_map[char]
    return sum

def singleByteXOR(a):
    a_bytearray = bytearray(a.decode('hex'))
    letters = [x for x in string.ascii_letters]
    freq_of_letters = []
    for key in letters:
        # or can reuse the old pgm, much cleaner :)
        new_key2 = key * len(a_bytearray)
        c = fixedXOR(a, new_key2.encode('hex')).decode('hex')
        freq_of_letters.append(calculateFrequency(c, new_key2))


if __name__ == '__main__':
    xor = singleByteXOR('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')