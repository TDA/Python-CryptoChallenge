__author__ = 'saipc'

import string
from fixedXOR import fixedXOR


def calculateFrequency(str, key):
    # the most frequent letters in the alphabet
    freq_map = {x: 0 for x in "etaoinshrdlu"}
    for char in str:
        if freq_map.has_key(char):
            # update occurrence
            freq_map[char] = freq_map[char] + 1
    sum = 0
    # return a count of all the letters
    for char in freq_map.keys():
        sum += freq_map[char]
    return sum

def singleByteXOR(a):
    length = len(a)
    letters = [x for x in string.ascii_letters]
    freq_of_letters = []
    for key in letters:
        # or can reuse the old pgm, much cleaner :)
        # encode the key and expand it to the length
        # of the string
        new_key2 = key.encode('hex') * length
        c = fixedXOR(a, new_key2)\
            .decode('hex')
        freq_of_letters.append(calculateFrequency(c, new_key2))
    # find the decoded string that is most similar to english
    max_match = max(freq_of_letters)
    return letters[freq_of_letters.index(max_match)]



if __name__ == '__main__':
    key = singleByteXOR('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print key, "is the key"