'''
Open html files and parse the information into json format
Best run from the root and using "input" when prompted
'''

import os
import codecs
from bs4 import BeautifulSoup
print "Enter a path relative to your current location:"
'''
userInput = raw_input()
'''
'''
path = os.path.abspath(userInput)
'''
path = "input"
print "userInput was " + path

L = [f for f in os.listdir(path) if not f.startswith('.')]

def doHTML(L):
    html = codecs.open(os.path.join(path, fileName),'r','utf-8').read()
    soup = BeautifulSoup(html, "html5lib")
    ''' title property '''
    title = soup.title.string.replace("BBC Food - Recipes - ","")
    print title
    matchTag = ["p", "a", "li"]
    matchAttr = ["class", "itemprop"]
    matchClass = ["recipe-metadata__prep-time", "recipe-metadata__cook-time", "recipe-metadata__serving", "recipe-metadata__dietary-vegetarian-text", "recipe-description__text", "recipe-metadata__recommendations", "author", "recipe-ingredients__list-item"]
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
                    elif ("recipe-ingredients" in matchClass[i]):
                        ingredient = elem.text
                        print ingredient
if not L.__len__() == 0:
    for index, fileName in enumerate(L):
        '''
        do the thing
        '''
        doHTML(L)
else:
    print "No files found"
