# -*- coding: utf-8 -*-
from gensim.corpora import WikiCorpus
import jieba
from langconv import *

def my_function():
    space = ' '
    i = 0
    l = []
    zhwiki_name = './data/zhwiki-latest-pages-articles.xml.bz2'
    f = open('./data/reduce_zhiwiki.txt', 'w',encoding='UTF-8')
    wiki = WikiCorpus(zhwiki_name, lemmatize=False, dictionary={})  #从xml文件中读出训练语料
    for text in wiki.get_texts():
        for temp_sentence in text:
            temp_sentence = Converter('zh-hans').convert(temp_sentence) #将语料中的繁体中文转化为简体中文
            seg_list = list(jieba.cut(temp_sentence))  #用jieba对语料中的句子进行分词
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')  #将分词好的句子写入文件
        l = []
        i = i + 1

        if (i %200 == 0):
            print('Saved ' + str(i) + ' articles')
    f.close()

if __name__ == '__main__':
    my_function()
