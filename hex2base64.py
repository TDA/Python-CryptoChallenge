__author__ = 'saipc'


def hex2base64 (str):
    return str.decode('hex').encode('base64')

if __name__ == '__main__':
    base64_string = hex2base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    print base64_string