# -*- coding:utf-8 -*-
import sys
import re
import time

alphabet = "abcdefghijklmnopqrstuvwxyz"
def word2edits1list(word):
    n = len(word)
    return list([word[0:i] + word[i+1:] for i in range(n)] +
               [word[0:i] + word[i+1] + word[i] + word[i+2:] for i in range(n-1)] +
               [word[0:i] + char + word[i+1:]  for i in range(n) for char in alphabet] +
               [word[0:i] + char + word[i:] for i in range(n+1) for char in alphabet] )

def open_word_dict():
    fin = open('en','r')
    correct_words = set()
    for word in fin:
        correct_words.add(word.rstrip())
    fin.close()
    return correct_words

def word2candidates2list(correct_words, wrong_word):
    return [word for word in correct_words if word in wrong_word]
#    for word in correct_words:
#        if word in wrong_word:
#            print word

def SearchWordFreq2list(candidate_words,wordfreqlist):
    freq2list = list()
    for word in wordfreqlist:
        for cword in candidate_words:
            if word[0] == cword:
                freq2list.append(word)
    return freq2list
#tab区切りファイルをリストで返す
def file2list(file_name):
    try:
        fin = open(file_name,'r')
    except:
        print 'リストで返すファイル名を間違えています'
    fin_list = list()
    fin_list = [line.rstrip().split('\t') for line in fin]
    fin.close()
    return fin_list

def tprint(data):
    for line in data:
        print "\t".join(line)

if __name__ == '__main__':
    print "brown_freq_list.txtを読み込み"
    brown_freq_list = file2list('brown_freq_list.txt')
    print "誤った単語を入力"
    try:
        st = raw_input().lower()
        wrong_word = word2edits1list(st)
    except:
        print "引数を1つ入力"
    time1 = time.clock()
    print "単語候補リスト作成中・・・"
    correct_words = open_word_dict()
    candidates = word2candidates2list(correct_words, wrong_word)

    print "辞書内での候補数:%d" %len(candidates)
    print candidates
    print "辞書と候補の比較中・・・"
    print "候補の単語\tbrownコーパスでの頻度"
    tprint(SearchWordFreq2list(candidates,brown_freq_list))
    time2 = time.clock()
    print "処理時間:%.2f秒" %(time2-time1)
