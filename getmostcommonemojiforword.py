#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import emojistools
import os
import gettweetswithword
from pathlib import Path
from collections import defaultdict

script, language = argv

frequencyboost = 1.1

def getMostCommonEmojiforword(word,printall,lang):

	freqtable = {}

	freqtablefile = open(os.path.abspath("/Users/oskar/Egna Dokument/Programmering/Emon/%s/emojifrequencies.csv" % lang))
	for row in freqtablefile.read().split("\n"):
		parts = row.split(";")
		if(len(parts)<2):continue
		key = parts[0]
		amount = parts[1]
		freqtable[key] = int(amount)

	sourcefilename = "%s/_emojitweets.txt" % lang


	sourcefile = open(sourcefilename)
	contents = sourcefile.read()
	sourcefile.close()

	emojislist = emojistools.loadEmojis()

	messageswithemoji = contents.split("\n")

	emojifrequency = {}
	foundMessages = 0
	for message in messageswithemoji:
		if word in message.split():
			foundMessages+=1
			for e in emojistools.getEmojisInText(message,emojislist):
				if e in emojifrequency:
					emojifrequency[e] += 1
				else:
					emojifrequency[e] = 1

	if(len(emojifrequency.keys())==0): return "none"
	r = list()

	mostUsed = "?"
	most = 0
	mostUsedWordsDict = defaultdict(int)

	for x in emojifrequency.keys():
		if(freqtable[x] > 1 and emojifrequency[x] > 1):
			rel = (emojifrequency[x]**frequencyboost) / freqtable[x]
			mostUsedWordsDict[x] += rel
			if(rel > most and freqtable[x] > 1 and emojifrequency[x] > 1):
				most = rel
				mostUsed = x

	if(printall):
		print("Found "+str(foundMessages))
		for item in sorted(mostUsedWordsDict, key=mostUsedWordsDict.get, reverse=False):
			usedPerc = mostUsedWordsDict[item]*100
			print ("%s  = %s" % (item, "{0:.2f}".format(usedPerc))+"%")

	#print (mostUsed + " (" + str(emojifrequency[x]) + " of " + str(foundMessages) + " messages)")
	return mostUsed

foundwords = {}
try:
	foundwordsfilepath = Path("%s/foundwords.csv" % language)
	if foundwordsfilepath.is_file():
		foundwordsfile = open(foundwordsfilepath)
		foundwordscontents = foundwordsfile.read()
		foundwordsfile.close()
	else:
		foundwordscontents = ""

	for row in foundwordscontents.split("\n"):
		parts = row.split(";")
		if(len(parts)<2):
			continue
		foundwords[parts[0]] = parts[1]
except RuntimeError:
	print ("Oops!")

ignored_words = emojistools.loadIgnoredWords()
emojislist=emojistools.loadEmojis()
instring = str(input(">"))
while instring != "close":
	words = gettweetswithword.Cleantweet(instring, emojislist,ignored_words).split()
	allemojis = ""
	for _word in words:
		printallw = len(words)==1
		if(not _word in foundwords.keys()):
			emoji = getMostCommonEmojiforword(_word,printallw,language)
			foundwords[_word] = emoji

		else:
				emoji = foundwords[_word]
		allemojis += emoji + "  "
		print (_word + "  =  " + emoji)

	if(len(allemojis) > 1): print ("\n" + allemojis)
	instring = str(input(">"))

destinationfile = open(foundwordsfilepath,'w')
for k in foundwords.keys():
	if(foundwords[k] != "?"):
		destinationfile.write(k+";"+foundwords[k]+"\n")

destinationfile.close()
