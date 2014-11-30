# -*- coding: utf8 -*-

from const import *
import re


class Article:
    def __init__(self, text):
        text = ' ' + text + ' '
        self.text = text
        text = re.sub('[\s,.?!\[\]\(\)]', ' ', text).lower()
        for stopWord in stopWords:
            text = text.replace(' ' + stopWord + ' ', ' ' * (len(stopWord) + 2))

        self.words = text.split()

        self.shingles = []
        for i in range(Article.shingleLength - 1, len(self.words), 1):
            self.shingles.append(self.words[i - Article.shingleLength + 1 : i + 1])
        self.isPlagiary = [False] * len(text)
        self.eText = text

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

    def highlight(self, sh):
        for m in re.finditer(sh, self.eText):
            rng = m.span()
            for i in range(rng[0], rng[1]):
                self.isPlagiary[i] = True

    def printShingles(self):
        for s in self.shingles:
            print ' '.join(s)

    def proc(self, openTag, closeTag):
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
