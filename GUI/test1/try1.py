import math
import operator
from textblob import TextBlob as tb
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import glob
import string
from tkinter import *
stop_words = set(stopwords.words("English"))

root = Tk()


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)


def idf(word, bloblist):
    x = n_containing(word, bloblist)
    return math.log(len(bloblist) / (x if x else 1))


# word is each word in all blobs
# blob is all words in document
# bloblist is corpus list
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


def stop_wordss(strings):
    list = []
    str = word_tokenize(strings)
    #P to add here
    for _ in str:

        if _ not in stop_words:
            list.append(_)

    returnstring = ' '.join(list)
    print("SSSSSSSSSSSSSS",returnstring, "\n\n\n\n")
    return returnstring

def unpunk(docs):
    intab = "!()-[]{};:'\"\,<>./?@#$%^&*_~"
    outtab = "                            "
    trantab = str.maketrans(intab, outtab)
    return str(docs.translate(trantab))

file_names = sorted(glob.glob("../../my_corpus/All/*"))
files = map(open, file_names)
documents = []
s = ""
for file in files:
    s=unpunk(file.read())
    print("HELLLLLLLLLLLLLOOOOO  :",s)
    stop_wordss(s)# like a toggle
    documents.append(s)
[file.close() for file in files]

doc_no_list = []
word_score = []
doc_score_dic = {}

word = "news"
bloblist = list(map(tb, documents))

for i, blob in enumerate(bloblist):
    # print("Score in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist)}
    # ^ dictionary of words with its value
    sorted_words = sorted(scores.items(), reverse=True)
    for word, score in sorted_words[:1]:
        s = score * 100
        word_score.append(s)
        doc_no_list.append(i + 1)
            # print("\tWord: {}, TF-IDF: {}".format(word, round(s, 5)))

doc_score_dic = dict(zip(doc_no_list, word_score))
# print(doc_score_dic)
sorted_doc_score = sorted(doc_score_dic.items(), key=operator.itemgetter(1), reverse=True)

    # print(sorted_doc_score)
for item in sorted_doc_score[:10]:
    print("Document: ", item[0], " has score : ", item[1])
