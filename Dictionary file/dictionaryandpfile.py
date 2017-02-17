from nltk.tokenize import word_tokenize,sent_tokenize

file = open('../my_corpus/All/JaD1.txt', 'r')
textexample =''
for i in file:
    textexample+=i
textexample= textexample.lower()

# for _ in sent_tokenize(textexample):
#     print(_)

for _ in word_tokenize(textexample):
    print(_)

#Give document based ID
#Remove duplicate words in dictionary file

