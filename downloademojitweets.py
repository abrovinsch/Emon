#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import sys
import gettweetswithword
import emojistools
import time
import datetime
import emojitweetslog
from sys import argv

script, lang = argv

emojis = emojistools.loadEmojis()
ignored_words = emojistools.loadIgnoredWords()

tweetsdownloaded = 0

result = ""
requests = 0
tweetsPerRequest = 10000

wordssourcefile = open("%s/words.txt" % lang)
wordscontents = wordssourcefile.read()
wordssourcefile.close()

words = wordscontents.split("\n")
totaldownloads = 0

for word in words:
    if(word.startswith("-") or len(word) == 0): continue

    emojitweetslog.log("Finding tweets with '%s'" % word)
    curDownloaded = 0
    tweetsfound = 0
    tweets = gettweetswithword.GetTweetsIncluding(word, lang, tweetsPerRequest)

    lasttweet=""
    while(tweets is None or tweets == 0):
        curtime = str(datetime.datetime.now().time())
        print("Sleeping for 15:15 minutes " +  curtime + "... Total downloads: %s" % totaldownloads)
        time.sleep(60*15.25)
        emojitweetslog.log("Done!")

        emojitweetslog.log("Finding tweets with '%s'" % word)
        tweets = gettweetswithword.GetTweetsIncluding(word, lang, tweetsPerRequest)

    for tweet in tweets:
        tweetsfound+=1
        if(tweet == lasttweet):
            continue
        lasttweet == tweet

        if(not tweet.startswith("RT") and emojistools.containsEmojis(tweet,emojis)):
            curDownloaded += 1
            tweet = gettweetswithword.Cleantweet(tweet,emojis,ignored_words)
            result += "\n" + tweet
            print("		    " + tweet)
            resultfile = open('%s/emojitweets.txt' % lang, 'r+')
            resultfile.write(result)
            resultfile.close()

    totaldownloads += curDownloaded
    emojitweetslog.log("Found %s, downloaded %s tweets." % (tweetsfound, curDownloaded))

    wordscontents = wordscontents.replace("\n"+word+"\n","\n-"+word+"\n")
    wordssourcefile = open("%s/words.txt" % lang,"w+")
    wordssourcefile.write(wordscontents)
    wordssourcefile.close()
