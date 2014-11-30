# -*- coding: utf8 -*-

from const import *
from article import *
import re

a = Article(article1DefaultText)
b = Article(article2DefaultText)

for s in Article.compare(a, b):
    print s
print ''.join([a.text[i] if a.isPlagiary[i] else '?' for i in range(len(a.text))])
print ''.join([b.text[i] if b.isPlagiary[i] else '?' for i in range(len(b.text))])
