# -*- coding: utf8 -*-

from const import *


class Article:
    def __init__(self, text):
        self.initialWords = text.split()
        self.words = filter(lambda x: not x in stopWords, self.initialWords)
        self.idx = []
        it = 0
        for i in range(len(self.words)):
            while self.initialWords[it] != self.words[i]:
                it += 1
            self.idx.append(it)
            it += 1

        self.shingles = []
        for i in range(shingleLength - 1, len(self.words), shingleLength - shingleLap):
            self.shingles.append(self.words[i - shingleLength + 1 : i + 1])

    @staticmethod
    def compare(article1, article2):
        sh1 = {' '.join(s) for s in article1.shingles}
        sh2 = {' '.join(s) for s in article2.shingles}
        res = set()

        for sh in sh1:
            if sh in sh2:
                res.add(sh)
        return res

    @staticmethod
    def highlight(text, shingle):
        wshingle = map(lambda x: '(' + x + ')', shingle)
        regex = '\s+'.join(wshingle)



a = Article('с1 с2 с3 с4 с5 с6 с7 с8 с9 с10')
b = Article('с1 с2 с3 с4 ф5 с6 с7 с8 с9 с10')

for shingle in Article.compare(a, b):
    print shingle
