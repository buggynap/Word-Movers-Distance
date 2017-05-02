dataset = list()

def loadDataSet():
	global dataset
	filePath = "processedBBC.txt"
	with open(filePath, 'r') as f:
		lines = f.read().split('\n')
		print lines
		for line in lines:
			line = line.split("#$#$#")
			if(len(line) == 2):
				text = line[1]
				label = line[0]
				item = [text, label]
				dataset.append(item)
	