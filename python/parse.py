'''
Open html files and parse the information into json format
Best run from the root and using "input" when prompted
'''

import os
import BeautifulSoup

print "Enter a path relative to your current location:"
userInput = raw_input()
path = os.path.abspath(userInput)
print "userInput was " + path

L = [f for f in os.listdir(path) if not f.startswith('.')]

if not L.__len__() == 0:
    for index, fileName in enumerate(L):
        print index, fileName
else:
    print "No files found"
