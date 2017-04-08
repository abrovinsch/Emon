#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import os

emojifilename = os.path.abspath("/Users/oskar/Egna Dokument/Programmering/Emon/emojis.txt")

def loadEmojis():
	emojiourcefile = open(emojifilename)
	emojiscontents = emojiourcefile.read()
	emojiourcefile.close()

	_emojis = emojiscontents.split("\n");
	return _emojis

def containsEmojis(t,_emojis):

	for e in _emojis:
		if e in t:
			return True
	return False

def getEmojisInText(m,_emojis):
	result = list()
	for e in _emojis:
		if(e in m and e not in result):
			result.append(e)

	return result

def containsText(t):
	alphabet = "abcdefghijklmnopqrstuvxyzåäöABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
	for letter in alphabet:
		if letter in t:
			return True
	return False

def loadIgnoredWords():
	ignored_words = ["pornstar","nigger","nigga","kike","aryan","milf","porn","tits","coon","whore","dildo","anus","anal"]
	return ignored_words
