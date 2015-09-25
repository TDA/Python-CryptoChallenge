__author__ = 'saipc'

from fixedXOR import *

def repeatingKeyXOR(a, key):
    # takes in plaintext and xors a key by repeating it across. ~ vigenere?
    length = len(a)
    key_length = len(key)
    key = str(key) * (length / key_length + 1)
    return fixedXOR(a.encode('hex'), key.encode('hex'))

if __name__ == '__main__':
    str1 = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    key = "ICE"
    xor = repeatingKeyXOR(str1, key)
    print xor