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
    key_range = [x for x in xrange(2,41)]
    with open('level6.txt', 'r') as file:
        data = file.read()
        decoded_data = data.decode('base64')
        # sum = calculateHammingDistance('this is a test', 'wokka wokka!!!')
        # print sum

    breakRepeatingKeyXOR()
