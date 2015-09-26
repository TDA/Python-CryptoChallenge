__author__ = 'saipc'

""" Input is a base64 encoded file that was earlier
encrypted using a repeating XOR"""

def breakRepeatingKeyXOR():
    return


def calculateHammingDistance(str1, str2):
    bin_str1  = ''.join(format(ord(x), 'b') for x in str1)
    bin_str2 = ''.join(format(ord(x), 'b') for x in str2)
    print bin_str2, bin_str1
    bin_str1 = bytearray(bin_str1)
    bin_str2 = bytearray(bin_str2)

    sum = 0
    for char in zip(bin_str1, bin_str2):
        print char
        sum += int(chr(char[0])) ^ int(chr(char[1]))
    print sum


if __name__ == '__main__':
    key_range = [x for x in xrange(2,41)]
    with open('level6.txt', 'r') as file:
        data = file.read()
        decoded_data = data.decode('base64')
        calculateHammingDistance('this is a test', 'wokka wokka!!!')

    breakRepeatingKeyXOR()
