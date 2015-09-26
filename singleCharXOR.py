__author__ = 'saipc'

from singlebyteXOR import *

if __name__ == '__main__':
    with open('level4.txt', 'r') as file:
        # def doesnt work, no idea why
        letters = [x for x in string.ascii_letters]
        matches = []
        for line in file:
            freq_of_letters = []
            line = line.strip('\n')
            line = line.encode('hex')
            length = len(line)
            for key in letters:
                new_key2 = key.encode('hex') * length
                c = fixedXOR(line, new_key2)\
                    .decode('hex')
                freq_of_letters.append(calculateFrequency(c, new_key2))
            # find the decoded string that is most similar to english
            matches.append(max(freq_of_letters))
        print max(matches)
        print matches
        #print letters[freq_of_letters.index(max_match)]

            #print line.decode('hex')




