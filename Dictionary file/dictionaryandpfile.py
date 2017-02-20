


def createTweetDict(inputDict):
    Dict = {}
    II = {}
    for Key, Text in inputDict.items():
        for word in Text.lower().split():
            II[word] = II.get(word,0)+1
            if Dict.get(word,False):
                if Key not in Dict[word]:
                    Dict[word].append(Key)
            else:
                Dict[word] = [Key]
    return Dict, II

def adddocument(filename):
    doc=''
    for _ in filename:
        doc+=_
    return doc

document_1 = open('../my_corpus/All/JaD1.txt', 'r')
document_2 = open('../my_corpus/All/JaD2.txt', 'r')
document_3 = open('../my_corpus/All/JaD3.txt', 'r')
document1=adddocument(document_1)
document2=adddocument(document_2)
document3=adddocument(document_3)

input ={1:document1, 2:document2, 3:document3}



Dic,InvI = createTweetDict(input)

print(Dic)

print(InvI)

































#
# from pprint import pprint as pp
# from glob import glob
#
# try:
#     reduce
# except:
#     from functools import reduce
# try:
#     raw_input
# except:
#     raw_input = input
#
#
# def parsetexts(fileglob='InvertedIndex/T*.txt'):
#     texts, words = {}, set()
#     for txtfile in glob(fileglob):
#         with open(txtfile, 'r') as f:
#             txt = f.read().split()
#             words |= set(txt)
#             texts[txtfile.split('\\')[-1]] = txt
#     return texts, words
#
#
# def termsearch(terms):  # Searches simple inverted index
#     return reduce(set.intersection,
#                   (invindex[term] for term in terms),
#                   set(texts.keys()))
#
#
# texts, words = parsetexts()
# print('\nTexts')
# pp(texts)
# print('\nWords')
# pp(sorted(words))
#
# invindex = {word: set(txt
#                       for txt, wrds in texts.items() if word in wrds)
#             for word in words}
# print('\nInverted Index')
# pp({k: sorted(v) for k, v in invindex.items()})
#
# terms = ["what", "is", "it"]
# print('\nTerm Search for: ' + repr(terms))
# pp(sorted(termsearch(terms)))