# -*- coding:utf-8 -*-
import sys
import re
import itertools

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_combi = [(x,y) for x in alphabet for y in alphabet]

fin = open('en', 'r')

for char in alphabet_combi:
    head = char[0] + char[1]
    fout = open('word_dic/'+head + '.txt','w')
    print head
    for line in fin:
        if len(line) < 2:
            continue
#            fout.writelines(line)
#一文字はスペルミスに含めない
        line_head = line[0].lower() + line[1]
        print head,line_head,line,
        if head == line_head:
            fout.writelines(line)
            print "○"
    fout.close()

fin.close()
