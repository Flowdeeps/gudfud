import os
import BeautifulSoup

print "Enter a path relative to your current location:"
userInput = raw_input()
path = os.path.abspath(userInput)
print "userInput was " + path

L = [f for f in os.listdir(path) if not f.startswith('.')]

if not L.__len__() == 0:
    print L
else:
    print "No files found"
