# -*- coding:utf-8 -*-
from nltk.corpus import brown
import nltk

fdist = nltk.FreqDist([w.lower() for w in brown.words()])

fout = open('brown_freq_list.txt', 'w')

for k,v in fdist.items():
    out_line = k + "\t" + str(v) + "\n"
    fout.writelines(out_line)

fout.close()
