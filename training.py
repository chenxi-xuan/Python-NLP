# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def my_function():
    wiki_news = open('./data/reduce_zhiwiki.txt', 'r',encoding='UTF-8')
    # 训练词向量，第一个参数是预处理后的训练语料库，sg=0,表示使用CBOW模型训练词向量；sg=1,表示使用Skip-gram训练词向量。参数size表示词向量的维度。
    #window表示当前词和预测词可能的最大距离，window越大所需要枚举的预测词越多，计算时间越长。min_count表示最小出现的次数，如果一个词语的出现次数
    #少于min_count，那么直接忽略该词。workers表示训练词向量时使用的线程数。
    model = Word2Vec(LineSentence(wiki_news), sg=0,size=192, window=5, min_count=5, workers=9)

    model.save('zhiwiki_news.word2vec')

if __name__ == '__main__':
    my_function()
