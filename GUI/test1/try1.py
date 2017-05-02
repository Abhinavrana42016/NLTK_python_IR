import math
import operator
from textblob import TextBlob as tb
from nltk.corpus import stopwords
import glob
from tkinter import *
from tkinter import ttk

stop_words = set(stopwords.words("English"))

root =Tk()


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)


def idf(word, bloblist):
    x = n_containing(word, bloblist)
    return math.log(len(bloblist) / (x if x else 1))

#word is each word in all blobs
#blob is all words in document
#bloblist is corpus list
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)





def insertword(thword):
    print("\nSearching for ",thword,"\n")
    file_names = sorted(glob.glob("../../my_corpus/All/*"))

    files=map(open,file_names)

    documents = [file.read() for file in files]
    [file.close() for file in files]

    doc_no_list=[]
    word_score=[]
    doc_score_dic={}

    word = thword
    bloblist = list(map(tb, documents))


    for i, blob in enumerate(bloblist):
        # print("Score in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) }
        # ^ dictionary of words with its value
        sorted_words = sorted(scores.items(), reverse=True)
        for word, score in sorted_words[:1]:
            s =score*100
            word_score.append(s)
            doc_no_list.append(i+1)
            # print("\tWord: {}, TF-IDF: {}".format(word, round(s, 5)))

    doc_score_dic = dict(zip(doc_no_list,word_score))
    # print(doc_score_dic)

    sorted_doc_score = sorted(doc_score_dic.items(), key=operator.itemgetter(1), reverse=True)

    # print(sorted_doc_score)
    for item in sorted_doc_score[:10]:
        print("Document: ",item[0]," has score : ",item[1])






def set_value(event):
    insertword(strVarible.get())




Label(root,text="Enter").grid(row=0,column=0,sticky=W,padx=4)
strVarible = StringVar()
strVarible.set("Enter query like \'news\'")
strEntry =  Entry(root,width=50,textvariable = strVarible).grid(row=0,column=1)


searchButton = Button(root,text="Search")
searchButton.grid(row=0,column=2,padx=4,pady=4)
searchButton.bind("<Button-1>",set_value)



Label(root,text="Options").grid(row=1,column=0,sticky=W)
Radiobutton(root,text="TF-IDF",value=1).grid(row=2,column=0,sticky=W)

Label(root,text="Filter").grid(row=1,column=1,sticky=W)
Checkbutton(root,text="StopWords").grid(row=2,column=1,sticky=W)



root.mainloop()