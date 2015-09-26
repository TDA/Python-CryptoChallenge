__author__ = 'saipc'

""" Input is a base64 encoded file that was earlier
encrypted using a repeating XOR"""

def breakRepeatingKeyXOR():
    return


def calculateHammingDistance(str1, str2):
    # hamming distance is merely the xor of the strings
    # first create equal length binary sequences, pad zeroes
    # if not equal --> 8 digit binary code for each one
    bin_str1  = ''.join('{0:08b}'.format(ord(x)) for x in str1)
    bin_str2 = ''.join('{0:08b}'.format(ord(x)) for x in str2)

    bin_str1 = bytearray(bin_str1)
    bin_str2 = bytearray(bin_str2)

    sum = 0
    for char in zip(bin_str1, bin_str2):
        sum += int(chr(char[0])) ^ int(chr(char[1]))
    return sum


if __name__ == '__main__':
    # generate key sizes from 2 to 40
    key_range = [x for x in xrange(2,41)]
    distances = []
    with open('level6.txt', 'r') as file:
        data = file.read().replace('\n', '')
        decoded_data = data.decode('base64')
        # sum = calculateHammingDistance('this is a test', 'wokka wokka!!!')
        # print sum
        for key in key_range:
            # calc and store the distances for each key
            str1 = data[0: key]
            str2 = data[key: 2 * key]
            distances.append((calculateHammingDistance(str1, str2)) / float(key))
        potential_indices = []
        # take the 3 lowest hamming distance causing keys
        for x in range(0, 3):
            index = distances.index(min(distances))
            distances.remove(distances[index])
            potential_indices.append(index)
        index = potential_indices[0]
        key = key_range[index]
        print index, key
        wordList = []
        for x in xrange(0, len(data), key):
            wordList.append(data[x : x+key])
        print wordList
    breakRepeatingKeyXOR()
