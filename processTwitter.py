# processing the data of BBC
import sys
import os
import re
import sys
import codecs

__author__ = "Ganesh Borle"

# -*- coding: utf-8 -*-

# This will store all the stopwords
stopWordsDict = dict()


# Function to load the stopwords from the file to the dictionary
def initDicts():
	# Global variable 
	global stopWordsDict
	# Open the file where all the stopwords are stored
	with open("stopWords.txt", 'r') as f:
		# For every word in file
		for word in f:
			# we get word as "word\n" so strip the '\n' and convert to lowercase
			stopWordsDict[word.rstrip('\n').lower()] = 1


# Remove the punctuation
def removePunctuation(text):
	return re.sub(r'[^\w\s]', '', text)


# Function to remove the stopwords
def removeStopWords(text):
	# stopWordsDict global dictionary
	global stopWordsDict
	newText = ''
	words = text.split()
	# For each word in that document
	for word in words:
		# Check if that word is stop word or not; if not then consider that word
		if word.lower() not in stopWordsDict:
			# Append that word to singledoc variable
			newText += word.lower() + ' '	
	# Return the list of all docs without stopwords
	return newText.rstrip(' ')

	
def processText(text):
	# Remove all new line
	text = text.replace("\n", " ")
	text = removePunctuation(text)
	# Remove the stop words
	text = removeStopWords(text)
	return text


def processDataNSave(fileName):
	outputFileName = "processedTwitter.txt"
	outputFileHandle = open(outputFileName, "wb+")
	with open(fileName, 'rb') as f:
		for line in f.read().split('\n'):
			if len(line.split('\t')) == 2:
				label, fileText = line.split('\t')
				fileText = fileText.decode('utf-8',errors='ignore')
		 	  	fileText = processText(fileText).encode('ascii', 'ignore')
		 	  	outputFileHandle.write(label + "#$#$#" + fileText + '\n')
	outputFileHandle.close()

if __name__ == '__main__':
	fileName = "/home/ganesh/Documents/IIITH/M-Tech/4-Sem/SMAI/Project/Final/Twitter/rawTweets.txt"
	processDataNSave(fileName)