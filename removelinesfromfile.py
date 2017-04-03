#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
import gettweetswithword

script, sourcefilename, forbiddenlinesfilename = argv

sourcefile = open(sourcefilename)
source = sourcefile.read()
sourcefile.close()

sourcelines = source.split("\n")

forbiddenlinesfile = open(forbiddenlinesfilename)
forbidden = forbiddenlinesfile.read()
forbiddenlinesfile.close()

forbiddenlines = forbidden.split("\n")

lines = list()
i = 0
print("starting to process %s lines..." % len(sourcelines))

print("Starting...")
size = len(sourcelines)
for l in sourcelines:
    i+=1
   	
    if(not l in forbiddenlines):
   	    lines.append(l)
    else:
   	    print("removed " + l)
		   
    #cleaned.append(tweet)
    if(i%(len(sourcelines)/20)==0):
        percentage = int((i/size)*100)
        print(str(percentage) + "%")

newcontents = ""
lines.sort()
for r in lines:
    newcontents += r + "\n"

destinationfile = open(sourcefilename,'w')
destinationfile.write(newcontents)
destinationfile.close()

print ("finished!")
