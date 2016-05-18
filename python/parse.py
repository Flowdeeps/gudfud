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
    title = soup.title.string.replace("BBC Food - Recipes - ","")
    print title ''' this is the title string '''

if not L.__len__() == 0:
    for index, fileName in enumerate(L):
        '''
        do the thing
        '''
        doHTML(L)
else:
    print "No files found"
