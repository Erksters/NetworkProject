import requests
import os
import time

# codeDictionary = {}
#
f = open("List.txt", "r")
f1 = f.readlines()
count = 0
secondCount = 0
for x in f1:
    x = x.replace("\n","")
    y = "https://www."+ x + ".com"
    print(y)
    try:

        WebURl = requests.head(y)
        count += 1
        print(WebURl.status_code)
        if(count == 300):
            break
    except:
        print("This Aint it")
        secondCount += 1

