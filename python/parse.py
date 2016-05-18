'''
Open html files and parse the information into json format
Best run from the root and using "input" when prompted
'''

import os
from bs4 import BeautifulSoup

print "Enter a path relative to your current location:"
userInput = raw_input()
path = os.path.abspath(userInput)
print "userInput was " + path

L = [f for f in os.listdir(path) if not f.startswith('.')]

def doHTML(L):
    html = open(os.path.join(path, fileName),'r').read()
    soup = BeautifulSoup(html, "html5lib")
    ''' title property '''
    title = soup.title.string.replace("BBC Food - Recipes - ","")
    print title
    matchClass = ["recipe-metadata__prep-time", "recipe-metadata__cook-time", "recipe-metadata__serving", "recipe-metadata__dietary-vegetarian-text", "recipe-description__text", "author"]
    for i in range(len(matchClass)):
        for para in soup.findAll("p", {"class": matchClass[i]}):
            if ("_prep" in matchClass[i]):
                prep = para.text
                print prep
            elif ("_cook" in matchClass[i]):
                cook = para.text
                print cook
            elif ("_serv" in matchClass[i]):
                serves = para.text
                print serves
            elif ("_diet" in matchClass[i]):
                vege = True
                print serves
            elif ("-desc" in matchClass[i]):
                desc = para.text
                print desc
        for anchor in soup.findAll("a", {"itemprop": matchClass[i]}):
            if ("auth" in matchClass[i]):
                author = anchor.text
                print author

if not L.__len__() == 0:
    for index, fileName in enumerate(L):
        '''
        do the thing
        '''
        doHTML(L)
else:
    print "No files found"
