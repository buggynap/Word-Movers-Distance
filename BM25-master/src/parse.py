__author__ = 'Nick Hirakawa'

import re


class CorpusParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')
		self.corpus = dict()

	def parse(self):
		with open(self.filename) as f:
			s = f.readlines()

		#print s	
		for x in s:
			x = x.split("#")
			text = x[1]
			docid = x[0]		 	
		 	self.corpus[docid] = text

		#print self.corpus

	def get_corpus(self):
		return self.corpus


class QueryParser:

	def __init__(self, filename):
		self.filename = filename
		self.queries = {}

	def parse(self):
		with open(self.filename) as f:
			x = f.readlines()
			for eachFIle in x:
				eachFIle = eachFIle.split("#")
				docid = eachFIle[0]
				line = eachFIle[1]
				self.queries[docid] = line.rstrip().split()

		# for i in self.queries:
		# 	print i,self.queries[i]
		#self.queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]

	def get_queries(self):
		return self.queries


if __name__ == '__main__':
	qp = QueryParser('text/queries.txt')
	print qp.get_queries()