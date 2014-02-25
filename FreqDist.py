# -*- coding:utf-8 -*-
import sys
import nltk

filename = raw_input()
text = nltk.filestring(open(filename))
word_tok = nltk.word_tokenize(text)
freqdist = nltk.FreqDist(word_tok)

for k,v in freqdist.items():
    print k,v
