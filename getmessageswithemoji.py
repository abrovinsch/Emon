#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import emojistools


script, smsfilename, emojifilename = argv

smssourcefile = open(smsfilename)
smscontents = smssourcefile.read()
smssourcefile.close()

text = ""
i = 0

lines =  smscontents.split("\r")
print(len(lines))

print("Going through messages")

messages = list()
for line in lines:
	i=i+1
	if(emojistools.containsEmojis(line,emojistools.loadEmojis()) and emojistools.containsText(line)):
		message = line.strip().lower()
		message = message.replace("Å","å")
		message = message.replace("Ä","ä")
		message = message.replace("Ö","ö")
		messages.append(message)

	if(i%500 == 0):
		percentage = str( int(i/float(len(lines)) * 100) )+"%"
		print(percentage)

messages.sort()

resultfile = open('messageswithemojiinthem.txt', 'w')
for message in messages:
  resultfile.write("%s\n" % message)
resultfile.close()
