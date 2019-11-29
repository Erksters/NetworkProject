import requests
import os
import time

# codeDictionary = {}
#
# f = open("List.txt", "r")
# f1 = f.readlines()
# for x in f1:
#     x = x.replace("\n","")
#     WebURl = urllib.request.urlopen("https://www."+ x + ".com")
#     print(codeDictionary.get(WebURl.getcode()))
#     time.sleep(3)

WebURl = requests.head("https://www." + "github" + ".com") # urlopen("https://www." + "aaaaa" + ".com")
print(WebURl.status_code)

