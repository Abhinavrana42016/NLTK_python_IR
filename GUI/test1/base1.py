import math
import operator
from textblob import TextBlob as tb
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import glob
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


def stop_wordss(strings,p):
    list = []
    str = word_tokenize(strings)
    #P to add here
    for _ in str:

        if _ not in stop_words:
            list.append(_)

    returnstring = ' '.join(list)
    print(returnstring, "\n\n\n\n")
    return returnstring


def insertword(thword, b,p):
    print("\nSearching for ", thword, "\n")
    file_names = sorted(glob.glob("../../my_corpus/All/*"))

    files = map(open, file_names)
    documents = []
    s = ""
    for file in files:
        s = file.read()
        if b: stop_wordss(s,p)

        documents.append(s)
    [file.close() for file in files]

    doc_no_list = []
    word_score = []
    doc_score_dic = {}

    word = thword
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


def set_value(event):
    insertword(strVarible.get(), booleanVar.get(),punchVar.get())


booleanVar = BooleanVar()
booleanVar.set(False)
punchVar = BooleanVar()
punchVar.set(False)

Label(root, text="Enter").grid(row=0, column=0, sticky=W, padx=4)
strVarible = StringVar()
strVarible.set("Enter one work query like \'news\'")
strEntry = Entry(root, width=50, textvariable=strVarible).grid(row=0, column=1)

searchButton = Button(root, text="Search")
searchButton.grid(row=0, column=2, padx=4, pady=4)
searchButton.bind("<Button-1>", set_value)

Label(root, text="Options").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="TF-IDF", value=1).grid(row=2, column=0, sticky=W)

Label(root, text="Filter").grid(row=1, column=1, sticky=W)
stopcheck = Checkbutton(root, text="StopWords", variable=booleanVar)
stopcheck.grid(row=2, column=1, sticky=W)

punchInCheck = Checkbutton(root, text="Remove Punctuation", variable=punchVar)
punchInCheck.grid(row=3, col=1, sticky=W)

root.mainloop()
