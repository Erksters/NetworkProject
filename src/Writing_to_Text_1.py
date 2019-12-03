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
length = 1               #01234 56789 10
text = addA(text,length) #aaaaa aaaaa a

f = open("List1.txt", "w+")

f.write(text+"\n")

for m in range(25):

    newChar = text[:1]
    text = dictionary[newChar]
    f.write(text+"\n")

print("DONE FAM")
