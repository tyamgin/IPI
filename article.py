# -*- coding: utf8 -*-

from const import *
import re
from utility import *


class FrequencyMatrix:
    def fillFromDocuments(self, docs):
        self.docs = docs    # документы
        self.docCount = {}  # количество документов по слову
        self.count = {}     # количество вхождений слова вообще

        for doc in docs:
            for word in doc.words:
                inc(self.docCount, word)
                inc(self.count, word, doc.words[word])

        self.words = [word for word in self.docCount if self.count[word] > 1]    # список популярных слов

        # удаление лишних слов
        wordsSet = {a for a in self.words}
        for doc in docs:
            doc.words = {word: doc.words[word] for word in doc.words if word in wordsSet}

        self.matrix = [[doc.count(word) for doc in docs] for word in self.words]
        # https://ru.wikipedia.org/wiki/TF-IDF
        for i in range(len(self.words)):
            idf = math.log(1.0 * len(self.docs) / self.docCount[self.words[i]])
            for j in range(len(self.docs)):
                self.matrix[i][j] *= idf

    def write(self, file_path=None):
        stream = getOutput(file_path)
        for i in range(len(self.words)):
            stream.write('%5s> %20s %s\n' % (i, self.words[i], ' '.join(['%2.6f' % i for i in self.matrix[i]])))
        closeOutput(stream)


class Article:
    def __init__(self, text):
        text = ' ' + text + ' '
        self.text = text
        text = re.sub('[\s,.?!\[\]\(\)]', ' ', text).lower()
        for stopWord in stopWords:
            text = text.replace(' ' + stopWord + ' ', ' ' * (len(stopWord) + 2))

        self.wordsList = text.split()
        self.words = {}
        for word in self.wordsList:
            inc(self.words, word)

        self.shingles = []
        for i in range(Article.shingleLength - 1, len(self.wordsList), 1):
            self.shingles.append(self.wordsList[i - Article.shingleLength + 1 : i + 1])
        self.isPlagiary = [False] * len(text)
        self.eText = text

    def count(self, word):
        return self.words[word] if word in self.words else 0

    def write(self):
        for key in self.words:
            print u'%20s %3s' % (key, self.words[key])

    # TODO: highlight & getColoredText можно делать быстрее
    def highlight(self, sh):
        for m in re.finditer(sh, self.eText):
            rng = m.span()
            for i in range(rng[0], rng[1]):
                self.isPlagiary[i] = True

    def getColoredText(self, openTag, closeTag):
        result = u''
        i = 0
        while i < len(self.text):
            if self.isPlagiary[i]:
                result += openTag
                j = i
                while j < len(self.text) and self.isPlagiary[j]:
                    result += self.text[j]
                    j += 1
                result += closeTag
                i = j
            else:
                result += self.text[i]
                i += 1
        return result

    def printShingles(self):
        for s in self.shingles:
            print ' '.join(s)



class IMatchComparer:
    @staticmethod
    def compare(article1, article2):
        matrix = FrequencyMatrix()
        matrix.fillFromDocuments([article1, article2])
        matrix.write()
        set1 = {matrix.words[i] for i in range(len(matrix.words)) if matrix.matrix[i][0] < 0.01}
        set2 = {matrix.words[i] for i in range(len(matrix.words)) if matrix.matrix[i][1] < 0.01}
        print len(set1)
        print len(set2)
        for word in set1:
            if word in set2:
                article1.highlight(u' ' + word + u' ')
                article2.highlight(u' ' + word + u' ')


class ShinglesComparer:
    @staticmethod
    def compare(article1, article2):
        sh1 = {' +'.join(s) for s in article1.shingles}
        sh2 = {' +'.join(s) for s in article2.shingles}
        res = set()

        for sh in sh1:
            if sh in sh2:
                article1.highlight(sh)
                article2.highlight(sh)
                res.add(sh)
        return res