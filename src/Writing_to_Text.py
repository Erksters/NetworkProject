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
length = 5               #01234 56789 10
text = addA(text,length) #aaaaa aaaaa a

f = open("List.txt", "w+")

f.write(text+"\n")

for m in range(26):

    for l in range(26):

        for k in range(26):

            for j in range(26):

                for i in range(26):
                    newChar = text[4:]
                    text = text[:4] + dictionary[newChar]
                    f.write(text+"\n")

                newChar = text[3:4]
                text = text[:3] + dictionary[newChar] + "a"
                f.write(text+"\n")

            newChar = text[2:3]
            text = text[:2] + dictionary[newChar] + "aa"
            f.write(text+"\n")

        newChar = text[1:2]
        text = text[:1] + dictionary[newChar] + "aaa"
        f.write(text+"\n")

    newChar = text[:1]
    text = dictionary[newChar] + "aaaa"
    f.write(text+"\n")

print("DONE FAM")
