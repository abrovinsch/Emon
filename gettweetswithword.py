#!/usr/bin/python
# -*- coding: utf-8 -*-

from TwitterSearch import *
import emojistools

def GetTweetsIncluding(word, language, max):

	try:
		tso = TwitterSearchOrder() # create a TwitterSearchOrder object
		tso.set_keywords([word]) # let's define all words we would like to have a look for
		if(language != ""): tso.set_language(language) # we want to see German tweets only
		tso.set_include_entities(False) # and don't give us all those entity information


		# it's about time to create a TwitterSearch object with our secret tokens
		tsA = TwitterSearch(
			consumer_key = 'pYtoes9l6uHd1Y7k4zjBFcuW9',
			consumer_secret = 'j0WSbdLbUmGxHialNGfkdpTxsF8kUmfDRUZuMY002lyNtORgHW',
			access_token = '223265942-Wc9qUlnqJ6RYGMCQdTHQu5FaNc54grfGIxJbOs0h',
			access_token_secret = '089FVa0IC5dmJWyNGLfUM9oPM94ixm79IuJiSg8VoM8ZD'
		)

		# Try the first acces token first, then the second then the third

		try:
			tweets = tsA.search_tweets_iterable(tso)

		except:
			  return 0

		result = list()
		i = 0
		for tweet in tweets:
			i+=1
			if(i>=max): break
			t = ( tweet['text'] )
			result.append(t)

		return result

		#print(twe)
	except TwitterSearchException as e: # take care of all those ugly errors if there are some
		print(e)

def Cleantweet(tweet,emojis, ignored_words):
	#ignored_words = ["pornstar","nigger","nigga","kike","aryan","milf","porn","tits","coon","whore","dildo","anus","anal"]

	tweet = tweet.replace("\n"," ")
	tweet = tweet.lower()

	tweetwithouthandles = ""
	for word in tweet.split():
		if(not word.startswith("@") and not word.startswith("t.co")and not word.startswith("http")and not word.startswith("bit.ly")):
			tweetwithouthandles += word + " "

	tweet = tweetwithouthandles

	symbolstoremove = "\"'•:;.?!$¢€§°´`¨^0123456789&+()[]{},…¶©£$∞§|≈±°””¥¢‰‰¶\}≠›•®†˙~¸˛√ªﬁøæ‘’‚…–°˝√‡˜ˆ∏˚◊∑∆∫¯˘¬º≥⁄ˇ«»“”„·¿˝"
	symbolstoreplace = "#+-\_–/=%<>*~—≤≤÷≈‹›"

	tweet = tweet.lower()

	tweet = tweet.replace("&amp;"," ")

	for symbol in symbolstoreplace:
		tweet = tweet.replace(symbol," ")

	for symbol in symbolstoremove:
		tweet = tweet.replace(symbol,"")

	emojisintweet = emojistools.getEmojisInText(tweet, emojis)

	for emoji in emojisintweet:
		tweet = tweet.replace(emoji," "+emoji+" ")

	already_included_emojis = list()

	tweetwithoutwithoutduplicatemojis=""

	for word in tweet.split():
		if(word in emojisintweet and not word in already_included_emojis):
			tweetwithoutwithoutduplicatemojis += word + " "
			already_included_emojis.append(word)
		elif(not word in already_included_emojis and not word in ignored_words):
			tweetwithoutwithoutduplicatemojis += word + " "

	tweet = tweetwithoutwithoutduplicatemojis

	return tweet.strip()
