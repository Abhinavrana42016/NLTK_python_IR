from collections import Counter
from math import sqrt


def word2vec(word):
    # count the characters in word
    cw = Counter(word)
    # precomputes a set of the different characters
    sw = set(cw)
    # precomputes the "length" of the word vector
    lw = sqrt(sum(c*c for c in cw.values()))

    # return a tuple
    return cw, sw, lw


def cosdis(v1, v2):
    # which characters are common to the two words?
    common = v1[1].intersection(v2[1])
    # by definition of cosine distance we have
    return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]


def adddocument(filename):
    doc=''
    for _ in filename:
        doc+=_
    return doc


document_1 = adddocument(open('../my_corpus/All/JaD1.txt', 'r'))
document_2 = adddocument(open('../my_corpus/All/JaD2.txt', 'r'))
document_3 = adddocument(open('../my_corpus/All/JaD3.txt', 'r'))
document1 = word2vec(document_1)
document2 = word2vec(document_2)
document3 = word2vec(document_3)
ddragon
print(" cosdis(document1,document2) : ")
print(cosdis("dragon",document2))
print(" cosdis(document1,document3) : ")
print(cosdis("dragon",document3))
print(" cosdis(document2,document3) : ")
print(cosdis("dragon",document3))




