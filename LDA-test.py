from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import codecs
import re
dataset = list()
#for i in range(0, lda.num_topics-1):
 #   print lda.print_topic(i)
tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()



def loadDataSet():
	global dataset
	filePath = "processedBBC.txt"
	with open(filePath, 'r') as f:
		lines = f.read().split('\n')
		for line in lines:
			line = line.split("#$#$#")
			if(len(line) == 2):
				text = line[1]
				label = line[0]
				item = [text, label]
				dataset.append(item)






def main():
  loadDataSet()
  lda_football=models.LdaModel.load('football.model')#loading trained and saved dataset for all 5 datasets 
  lda_cricket=models.LdaModel.load('cricket.model')
  lda_atheletics=models.LdaModel.load('atheletics.model')
  lda_rugby= models.LdaModel.load('rugby.model')
  lda_tennis =  models.LdaModel.load('tennis.model')

  for i in dataset:
  	texts=[]
  	raw = i[0].lower()
   
   	tokens=tokenizer.tokenize(raw)
    # remove stop words from tokens
   	stopped_tokens = [k for k in tokens if not k in en_stop]
    # stem tokens
   	stemmed_tokens = [p_stemmer.stem(j) for j in stopped_tokens]
    # add tokens to list
   	texts.append(stemmed_tokens)
	# turn our tokenized documents into a id <-> term dictionary
	dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
	corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model from testing dataset
	ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=20)
   	l=ldamodel.show_topics(num_topics=5, num_words=1)
   	doc_lda = ldamodel[corpus]
   	doc_football = ldamodel[corpus]
   	doc_cricket = ldamodel[corpus]
   	doc_rugby = ldamodel[corpus]
   	doc_lennis = ldamodel[corpus]
   	print i[1] 
   	print l
if __name__== "__main__":
  main()
