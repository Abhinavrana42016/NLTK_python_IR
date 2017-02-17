import string
from string import punctuation

from numpy.core.defchararray import lower
from nltk.stem import PorterStemmer
from nltk.tokenize import *
from nltk.corpus import stopwords



punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
document_1 = open('../../my_corpus/All/JaD1.txt', 'r')
doc =''

for _ in document_1:
    doc+=_.lower()

print(doc)
print('+++++++++++++++++++++++++++++++++++++++++++++++++')

# Remove punctuations
# fast alternative  #doc.translate(None, string.punctuation)
doc_without_punctuation=''
for w in doc:
    if w not in punctuation:
        doc_without_punctuation += w
print(doc_without_punctuation)

# Now tokenize remove duplicates

ps =PorterStemmer()
doc_tokenized = set(word_tokenize(doc_without_punctuation))
doc_stemmed = ''
for w in doc_tokenized:
    print(w +" Stemmed to :    " + ps.stem(w))


