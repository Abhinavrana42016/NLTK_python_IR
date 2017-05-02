import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer,word_tokenize


train_text =state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custon_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custon_sent_tokenizer.tokenize(sample_text)



def process_content():
    try:
        for i in tokenized:
            words = word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)

            chunkGram =r'''Chunk:{<RB.?>*<VB.?>*<NNP><NN>?}'''

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)




    except Exception as e:

        print(str(e))

process_content()


