import math
# import re
from textblob import TextBlob as tb


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


def adddocument(filename):
    doc=''
    for _ in filename:
        doc+=_
    return doc


document_1 = open('../my_corpus/All/JaD1.txt', 'r')
document_2 = open('../my_corpus/All/JaD2.txt', 'r')
document_3 = open('../my_corpus/All/JaD3.txt', 'r')
document1=tb(adddocument(document_1))
document2=tb(adddocument(document_2))
document3=tb(adddocument(document_3))

#using regex punctation removal
# remove_punc=r"(\w+)"
# word =re.findall(remove_punc,str(document1))
# print(word)
print("PRINTING DOCUMNT 1\n : : \n ",document1)

bloblist = [document1, document2, document3]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    # ^ dictionary of words with its value
    sorted_words = sorted(scores.items(), reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))