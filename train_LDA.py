from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import codecs
import re
tokenizer = RegexpTokenizer(r'\w+')
# create English stop words list
en_stop = get_stop_words('en')
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
texts = []
for i in range(1,101):
	if i<10:
		doc="00"+str(i)
	elif i<100:
		doc="0"+str(i)
	else:
		doc="100"
	doc=doc+".txt"
	f=codecs.open(doc,"r",encoding='utf8')
	s=f.read()
	raw = s.lower()
	result = ''.join(i for i in raw if not i.isdigit())
   	result2=re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', result)
   	tokens = tokenizer.tokenize(result2)

   	# remove stop words from tokens
   	stopped_tokens = [j for j in tokens if not j in en_stop]
    
    # stem tokens
  	stemmed_tokens = [p_stemmer.stem(z) for z in stopped_tokens]
    
    # add tokens to list
   	texts.append(stemmed_tokens)
   	#print texts
# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=100, id2word = dictionary, passes=10)
ldamodel.save('/home/vivek/BookMyCab/Desktop/SMAI/bbcsport/test/tennis.model')



