#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
import gettweetswithword
import emojistools
import emojitweetslog

script, sourcefilename = argv

sourcefile = open(sourcefilename,"r")
contents = sourcefile.read()
sourcefile.close()

cleaned = list()
i = 0
tweets = contents.split("\n")
emojitweetslog.log("starting to process %s lines..." % len(tweets))

emojitweetslog.log("Cleaning...")
size = len(tweets)

emojis = emojistools.loadEmojis()
ignored_words = emojistools.loadIgnoredWords()
for tweet in tweets:
    i+=1
    cleaned.append(gettweetswithword.Cleantweet(tweet,emojis,ignored_words))
    #cleaned.append(tweet)
    if(i%int(len(tweets)/20)==0):
        percentage = int((i/size)*100)
        print(str(percentage) + "%")


emojitweetslog.log("Removing duplicates...")
withoutduplicates = list()

i=0
removed = 0
lasttweet = ""
cleaned.sort()
for tweet in cleaned:

    leng = int(len(lasttweet)*0.75)

    if(tweet == lasttweet):
        removed+=1
        print("Remove duplicate:")
        print(lasttweet)
        print(tweet)

    elif(len(tweet) >= 40 and len(lasttweet) >= 40 and tweet.startswith(lasttweet[0:leng])):
        removed+=1
        print("Remove near duplicate:")
        print(lasttweet[0:leng])
        print(tweet)
    else:
        withoutduplicates.append(tweet)
        lasttweet = tweet

    if(i%int(len(cleaned)/20)==0):
        percentage = int(i/len(tweets)*100)
        print(str(percentage) + "%")
    i+=1

emojitweetslog.log("Removed %s items" % removed)

newcontents = ""
withoutduplicates.sort()
for r in withoutduplicates:
    newcontents += r + "\n"

destinationfile = open(sourcefilename,'w')
destinationfile.seek(0)
destinationfile.write(newcontents)
destinationfile.close()
