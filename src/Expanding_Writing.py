import os

def addA(string, numTimes):
    '''
    This method will return a list of numTimes long
    :param string:
    :type string:
    :param numTimes:
    :type numTimes:
    :return string:
    :rtype string:
    '''
    for x in range(numTimes):
        string += 'a'
    return string

'''This is the dictionary used withing the loops to exchange letters for their next counterpart '''
dictionary = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e': 'f','f':'g', 'g':'h',
              'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o',
              'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w',
              'w':'x', 'x':'y', 'y':'z', 'z':'z'}

text = ""
length = 11               #01234 56789 10
text = addA(text,length) #aaaaa aaaaa a

f = open("List2.txt", "w+")

f.write(text+"\n")
for s in range(26):

    for r in range(26):

        for q in range(26):

            for p in range(26):

                for o in range(26):

                    for n in range(26):

                        for m in range(26):

                            for l in range(26):

                                for k in range(26):

                                    for j in range(26):

                                        for i in range(26):                         #Start editing the last character
                                            newChar = text[10:]
                                            text = text[:10] + dictionary[newChar]
                                            f.write(text+"\n")

                                        newChar = text[9:10]                        #Then work your way back in the nested for loop
                                        text = text[:9] + dictionary[newChar] + "a"
                                        f.write(text+"\n")

                                    newChar = text[8:9]
                                    text = text[:8] + dictionary[newChar] + "aa"
                                    f.write(text+"\n")

                                newChar = text[7:8]
                                text = text[:7] + dictionary[newChar] + "aaa"
                                f.write(text+"\n")

                            newChar = text[6:7]
                            text = text[:6] +dictionary[newChar] + "aaaa"
                            f.write(text+"\n")

                        newChar = text[5:6]
                        text = text[:5] + dictionary[newChar] + "aaaaa"
                        f.write(text + "\n")

                    newChar = text[4:5]
                    text = text[:4] + dictionary[newChar] + "aaaaaa"
                    f.write(text + "\n")

                newChar = text[3:4]
                text = text[:3] + dictionary[newChar] + "aaaaaaa"
                f.write(text + "\n")

            newChar = text[2:3]
            text = text[:2] + dictionary[newChar] + "aaaaaaaa"
            f.write(text + "\n")

        newChar = text[1:2]
        text = text[:1] + dictionary[newChar] + "aaaaaaaaa"
        f.write(text + "\n")

    newChar = text[:1]
    text = dictionary[newChar] + "aaaaaaaaaa"
    f.write(text + "\n")

print("DONE FAM")

