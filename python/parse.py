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
    matchTag = ["p", "a"]
    matchAttr = ["class", "itemprop"]
    matchClass = ["recipe-metadata__prep-time", "recipe-metadata__cook-time", "recipe-metadata__serving", "recipe-metadata__dietary-vegetarian-text", "recipe-description__text", "recipe-metadata__recommendations", "author"]
    for j in range(len(matchTag)):
        for n in range(len(matchAttr)):
            for i in range(len(matchClass)):
                for elem in soup.findAll(matchTag[j], {matchAttr[n]: matchClass[i]}):
                    if ("_prep" in matchClass[i]):
                        prep = elem.text
                        print "prep: " + prep
                    elif ("_cook" in matchClass[i]):
                        cook = elem.text
                        print "cook: " + cook
                    elif ("_serv" in matchClass[i]):
                        serves = elem.text
                        print "serves: " + serves
                    elif ("_diet" in matchClass[i]):
                        vege = True
                        print "Vegetarian"
                    elif ("_recom" in matchClass[i]):
                        recommend = elem.text
                        print "recommended: " + recommend
                    elif ("-desc" in matchClass[i]):
                        desc = elem.text
                        print "description: " + desc
                    elif ("auth" in matchClass[i]):
                        author = elem
                        if not author.img:
                            author = elem.text
                            print "author: " + author
if not L.__len__() == 0:
    for index, fileName in enumerate(L):
        '''
        do the thing
        '''
        doHTML(L)
else:
    print "No files found"
