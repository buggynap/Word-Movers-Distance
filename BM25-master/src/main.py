__author__ = 'Nick Hirakawa'


from parse import *
from query import QueryProcessor
import operator


def main():
	qp = QueryParser(filename='../text/quer.txt')
	qp.parse()
	cp = CorpusParser(filename='../text/corps.txt')
	queries = qp.get_queries()
	cp.parse()
	corpus = cp.get_corpus()
	proc = QueryProcessor(queries, corpus)
	results,originalResults = proc.run()
	qid = 0
	total = 10
	correct =0
	for result in results:
		sorted_x = sorted(result.iteritems(), key=operator.itemgetter(1))
		sorted_x.reverse()
		index = 0
		#print sorted_x[0]
		try:
			actualOutput = sorted_x[0][0]
			expected = originalResults[qid]	
			actualOutput = actualOutput.split("-")[0].strip()
			expected = expected.split("-")[0].strip()
			#print actualOutput,expected
			if actualOutput == expected:
				correct+=1
			total+=1
		except Exception as e:
			pass
		
		qid += 1

	print ("Accuracy"),
	print((correct/float(total))*100)


if __name__ == '__main__':
	main()