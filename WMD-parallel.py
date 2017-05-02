import sys
import os
import numpy as np
import re
import random
import math
from math import log
from gensim.models import KeyedVectors
import  multiprocessing
from functools import partial
import time

__author__ = "Ganesh Borle"

# This will store all the stopwords
stopWordsDict = dict()

word2VecModel = None

dataset = list()

def loadDataSet():
	global dataset
	filePath = "/home/ganesh/Documents/IIITH/M-Tech/4-Sem/SMAI/Project/processedBBC.txt"
	with open(filePath, 'r') as f:
		lines = f.read().split('\n')
		for line in lines:
			line = line.split("#$#$#")
			if(len(line) == 2):
				text = line[1]
				label = line[0]
				item = [text, label]
				dataset.append(item)

# Euclidean distance calculator
def euclideanDistance(word1, word2):
	dist = np.linalg.norm(word1 - word2)
	return dist

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

def initWord2Vec():
	global word2VecModel
	print("Loading word2VecModel")
	word2VecModel = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True)	
	print("word2VecModel Loaded")


def getScoreOfTwoDocs(query, document):
	global word2VecModel
	querySet = set(query.split())
	documentSet = set(document.split())
	score = 0.0
	for queryWord in querySet:
		try:
			queryWordVector = word2VecModel[queryWord]
			if not documentSet:
				continue;
			miniDist = 1e+7
			miniword = ''
			for documentWord in documentSet:
				try:
					dist = euclideanDistance(queryWordVector, word2VecModel[documentWord])
				except Exception as e:
					dist = 1e100			
				if miniDist >= dist:
					miniDist = dist
					miniword = documentWord
			score = score + miniDist
			documentSet.remove(miniword)
		except Exception as e:
			pass
	return score


def getNearLabel(testtextWords, trainData):
	predictedLabel = ""
	minScore = 1e10
	for doc in trainData:
		trainText, trainLabel = doc[0], doc[1]
		print("Checking with : " + trainLabel)
		currentScore = getScoreOfTwoDocs(testtextWords, trainText)
		if(currentScore < minScore):
			predictedLabel = trainLabel
			minScore = currentScore
	return predictedLabel

					
def WMDScore():
	global word2VecModel
	global dataset
	pool = multiprocessing.Pool()
	accuracyList = list()	
	random.shuffle(dataset)
	totalDocs = len(dataset)
	# 80-20 split
	error = 0
	trainData, testData = dataset[:int(0.8*totalDocs)], dataset[int(totalDocs*0.8) + 1:totalDocs]
	#pool.map(getNearLabel, (testData, trainData))
	for docInTest in testData:
		testtextWords, testLabel = docInTest[0], docInTest[1]
		# Setting two parameters
		func = partial(getNearLabel, testtextWords)
		predictedLabel = pool.map(func,trainData)
		pool.close()
		pool.join()
		#predictedLabel = getNearLabel(testtextWords, trainData)
		print("predictedLabel : " + predictedLabel + " Correct Label : " + testLabel)
		if(predictedLabel != testLabel):
			error = error + 1
	print ("Accuracy : " + str((len(testData) - error)*100/len(testData)))


# Function to remove the stopwords
def removeStopWords(docList):
	# stopWordsDict global dictionary
	global stopWordsDict
	# List of docs which will contains all the words without the stopwords
	newdocList = []
	for doc in docList:
		# Single doc to store the words without stopwords
		newDoc = ''
		# Split on the basis of space
		words = doc.split()
		# For each word in that document
		for word in words:
			# Check if that word is stop word or not; if not then consider that word
			if word.lower() not in stopWordsDict:
				# Append that word to singledoc variable
				newDoc += word.lower() + ' '
		# Append the singledoc to the list of docs
		newdocList.append(newDoc.rstrip(' '))
	# Return the list of all docs without stopwords
	return newdocList

# Remove the punctuation
def removePunctuation(docList):
	# list of all docs without any punchutation mark 
	newdocList = []
	# For evey doc in docList
	for doc in docList:
		# Remove all the punctutation marks using re
		doc = re.sub(r'[^\w\s]', '', doc)
		# Append to the new list
		newdocList.append(doc)
	# Return the updated list
	return newdocList

def init():
	# Init pre required stuff
	#initDicts()
	# Init word2vec model
	initWord2Vec()
	loadDataSet()
	WMDScore()

if __name__ == '__main__':
	init()