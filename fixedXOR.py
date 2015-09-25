__author__ = 'saipc'


def fixedXOR(a, b):
    # decode from hex
    a = a.decode('hex')
    b = b.decode('hex')
    # convert to bytes
    a_bytearray = bytearray(a)
    b_byteaaray = bytearray(b)
    c_bytearray = bytearray(len(a_bytearray))
    # print a_bytearray, b_byteaaray
    # fixed length buffers, so enough to check one length
    for x in xrange(0, len(a)):
        # xor
        c_bytearray[x] = a_bytearray[x] ^ b_byteaaray[x]
    # decode bytes to string, and then encode back to hex
    # print c_bytearray
    c = (c_bytearray).decode('utf-8').encode('hex')

    return c



if __name__ == '__main__':
    xor = fixedXOR('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    print xor
