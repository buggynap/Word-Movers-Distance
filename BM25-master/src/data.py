import numpy as np
#from numpy import *
import numpy.matlib
import math, time
from tempfile import TemporaryFile
import pickle

def loadDataSet():
	global dataset
	filePath = "/home/sam/Downloads/BM25-master/text/processedBBC1.txt"
	
	with open(filePath, 'r') as f:
		lines = f.read().split('\n')
		for line in lines:
			line = line.split("#$#$#")
			if(len(line) == 2):
				text = line[1]
				label = line[0]
				item = [text, label]
				dataset.append(item)


dataset = list()
#category = ["tennis","rugby","football","cricket","athletics"]
#labels = {"tennis":0,"rugby":1,"football":2,"cricket":3,"athletics":4}
totalVoc = {}
totalWordListWithIndex = {}
loadDataSet()
import random
random.shuffle(dataset)
testData = []
trainData = []
testLabel = []
trainLabel = []
totalDocs = len(dataset)
trainData1, testData1 = dataset[:int(0.8*totalDocs)], dataset[int(totalDocs*0.8) + 1:totalDocs]

f1 = open("/home/sam/Downloads/BM25-master/text/corps.txt","w")
i = 0
for eachrow in trainData1:
	eachdoc =eachrow[1]+"-"+str(i)+"#"+eachrow[0]
	f1.write(eachdoc)
	f1.write("\n")
	i+=1

f1.close()

f2 = open("/home/sam/Downloads/BM25-master/text/quer.txt","w")
i = 0
for eachrow in testData1:
	eachdoc =eachrow[1]+"-"+str(i)+"#"+eachrow[0]
	f2.write(eachdoc)
	f2.write("\n")
	i+=1

f2.close()


# size = len(totalWordListWithIndex.items())

# ################ making bag of word model ########################
# bowDict = {}
# for eachlist in dataset:
# 	eachlist1 = eachlist[0].split()
# 	l = [0]*size
# 	for eachWord in eachlist1:
# 		l[totalWordListWithIndex[eachWord]]+=1

# 	t = tuple(l)
# 	#print eachlist[1]
# 	bowDict[t] = labels[eachlist[1]]

# leng = int(0.8*len(bowDict))
# testData = []
# trainData = []
# testLabel = []
# trainLabel = []
# i = 1
# for each in bowDict:

# 	if i != 1:
# 		l = list(each)
# 		trainData.append(l)
# 		trainLabel.append(bowDict[each])

# 	i+=1

# i = 1

# for each in bowDict:

# 	if i <= 5:
# 		l = list(each)
# 		testData.append(l)
# 		testLabel.append(bowDict[each])
# 		i+=1

#pickle.dump((trainData, trainLabel, testData, testLabel), open("/home/sam/Documents/coding/raw_text_dataset.pickle", "wb"))

# testData = np.array(testData)
# trainData = np.array(trainData)
# testLabel = np.array(testLabel)
# trainLabel = np.array(trainLabel)

# np.save('train_data.npy', trainData)

# np.save('test_data.npy', testData)

# np.save('test_labels.npy', testLabel)

# np.save('train_labels.npy', trainLabel)

