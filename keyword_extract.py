# -*- coding: utf-8 -*-
import jieba.posseg as pseg
from jieba import analyse

def keyword_extract(data, file_name):   #提取句子的关键词
   tfidf = analyse.extract_tags
   keywords = tfidf(data)
   return keywords

def getKeywords(docpath, savepath):    #将每句话进行关键词提取，并将关键词保存在txt文件

   with open(docpath, 'r',encoding='UTF-8') as docf, open(savepath, 'w',encoding='UTF-8') as outf:
      for data in docf:
         data = data[:len(data)-1]
         keywords = keyword_extract(data, savepath)
         for word in keywords:
            outf.write(word + ' ')
         outf.write('\n')
