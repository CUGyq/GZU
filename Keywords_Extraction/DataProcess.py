#! -*- coding: utf-8 -*-
#date 13/5/2019
import re
import jieba.posseg as pseg
class processData():
    def __init__(self,text,fname):
        '''

        :param text: input text
        :param fname:stopwords_text name
        '''
        self.text=text
        self.fname=fname
    def process(self):
        text = re.sub("[！？...]", "。", self.text.strip()) # with '。' replace those punctuation
        filter=["n","nr","ns","nt","nl","ng","vn","v"]
        stopwords=self.getStopwords()  #load stopwords
        wordsall_list=[]  #all words in text
        for sentence in text.strip().split("。"):
            tempwords_list=[]
            cuted_words=pseg.cut(sentence,HMM=True)  #cuted words
            for w in cuted_words:
                if w.word not in stopwords and w.flag in filter:
                    tempwords_list.append(w.word)
            wordsall_list.append(tempwords_list)
        return wordsall_list
    def getStopwords(self):
        stopwords=[line.strip() for line in open(self.fname,'r',encoding="utf-8").readlines()]
        return stopwords

