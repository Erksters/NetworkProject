import os

def addA(string, numTimes):
    for x in range(numTimes):
        string += 'a'
    return string

dictionary = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e': 'f','f':'g', 'g':'h',
              'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o',
              'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w',
              'w':'x', 'x':'y', 'y':'z', 'z':'z'}

text = ""
length = 6                #01234 56789 10
text = addA(text, length) #aaaaa aaaaa a

f = open("List6.txt", "w+")

f.write(text+"\n")
for n in range(26):

    for m in range(26):

        for l in range(26):

            for k in range(26):

                for j in range(26):

                    for i in range(25):

                        newChar = text[5:]
                        text = text[:5] + dictionary[newChar]
                        f.write(text + "\n")

                    newChar = text[4:5]
                    if (newChar != 'z'):
                        text = text[:4] + dictionary[newChar] + "a"
                        f.write(text+"\n")

                newChar = text[3:4]
                if (newChar != 'z'):
                    text = text[:3] + dictionary[newChar] + "aa"
                    f.write(text+"\n")

            newChar = text[2:3]
            if(newChar != 'z'):
                text = text[:2] + dictionary[newChar] + "aaa"
                f.write(text+"\n")

        newChar = text[1:2]
        if (newChar != 'z'):
            text = text[:1] + dictionary[newChar] + "aaaa"
            f.write(text + "\n")

    newChar = text[:1]
    if (newChar != 'z'):
        text = dictionary[newChar] + "aaaaa"
        f.write(text+"\n")

print("DONE FAM")
