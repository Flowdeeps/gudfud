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
    matchClass = ["recipe-metadata__prep-time", "recipe-metadata__cook-time", "recipe-metadata__serving", "recipe-metadata__dietary-vegetarian-text"]
    for i in range(len(matchClass)):
        for para in soup.findAll("p", {"class": matchClass[i]}):
            if ("_prep" in matchClass[i]):
                prep = para.text
                print prep
            if ("_cook" in matchClass[i]):
                cook = para.text
                print cook
            if ("_serv" in matchClass[i]):
                serves = para.text
                print serves
            if ("_diet" in matchClass[i]):
                vege = True
                print serves

if not L.__len__() == 0:
    for index, fileName in enumerate(L):
        '''
        do the thing
        '''
        doHTML(L)
else:
    print "No files found"
