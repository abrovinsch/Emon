#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
import emojistools

script, sourcefilename, destinationfilename = argv

sourcefile = open(sourcefilename)
contents = sourcefile.read()
sourcefile.close()

freqtable = {}

emojis = emojistools.loadEmojis()

for e in emojis:
    freqtable[e] = 0

i = 0
tweets = contents.split("\n")
for tweet in tweets:
    i+=1
	
	  #actually do the counting
    for word in tweet.split():
        if(emojistools.containsEmojis(word,emojis)):
			      freqtable[word] = freqtable[word]+1
	
    if(i%int(len(tweets)/20)==0):
        percentage = int((i/len(tweets))*100)
        print(str(percentage) + "%")

result = ""

for key in freqtable:
	result += key + ";" + str(freqtable[key]) + "\n"

destinationfile = open(destinationfilename,'w')
destinationfile.write(result)
destinationfile.close()