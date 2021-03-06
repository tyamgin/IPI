# -*- coding: utf8 -*-

article1DefaultText = '''Канонизация текста приводит оригинальный текст к единой нормальной форме. Текст очищается от предлогов, союзов, знаков препинания, HTML тегов, и прочего ненужного «мусора», который не должен участвовать в сравнении. В большинстве случаев также предлагается удалять из текста прилагательные, так как они не несут смысловой нагрузки.

Также на этапе канонизации текста можно приводить существительные к именительному падежу, единственному числу, либо оставлять от них только корни.

Желательно НЕ ЗАБЫТЬ бы перевести все буквы в один регистр.'''

article2DefaultText = '''Канонизация текста приводит текст к единой нормальной форме. Он очищается от предлогов, союзов, знаков препинания, html тегов, и прочего текста, который не должен участвовать в сравнении. На этапе канонизации текста можно приводить существительные к именительному падежу, единственному числу, либо оставлять от них только корни.

Так как они не несут смысловой нагрузки, нужно удалять из текста прилагательные.

И не забыть перевести все буквы в нижний регистр.'''

stopWords = {u'еще', u'него', u'сказать', u'а', u'ж', u'нее', u'со', u'без', u'же', u'ней', u'совсем', u'более', u'жизнь', u'нельзя', u'так', u'больше', u'за', u'нет', u'такой', u'будет', u'зачем', u'ни', u'там', u'будто', u'здесь', u'нибудь', u'тебя', u'бы', u'и', u'никогда', u'тем', u'был', u'из', u'ним', u'теперь', u'была', u'из-за', u'них', u'то', u'были', u'или', u'ничего', u'тогда', u'было', u'им', u'но', u'того', u'быть', u'иногда', u'ну', u'тоже', u'в', u'их', u'о', u'только', u'вам', u'к', u'об', u'том', u'вас', u'кажется', u'один', u'тот', u'вдруг', u'как', u'он', u'три', u'ведь', u'какая', u'она', u'тут', u'во', u'какой', u'они', u'ты', u'вот', u'когда', u'опять', u'у', u'впрочем', u'конечно', u'от', u'уж', u'все', u'которого', u'перед', u'уже', u'всегда', u'которые', u'по', u'хорошо', u'всего', u'кто', u'под', u'хоть', u'всех', u'куда', u'после', u'чего', u'всю', u'ли', u'потом', u'человек', u'вы', u'лучше', u'потому', u'чем', u'г', u'между', u'почти', u'через', u'где', u'меня', u'при', u'что', u'говорил', u'мне', u'про', u'чтоб', u'да', u'много', u'раз', u'чтобы', u'даже', u'может', u'разве', u'чуть', u'два', u'можно', u'с', u'эти', u'для', u'мой', u'сам', u'этого', u'до', u'моя', u'свое', u'этой', u'другой', u'мы', u'свою', u'этом', u'его', u'на', u'себе', u'этот', u'ее', u'над', u'себя', u'эту', u'ей', u'надо', u'сегодня', u'я', u'ему', u'наконец', u'сейчас', u'если', u'нас', u'сказал', u'есть', u'не', u'сказала'}
defaultShingleLength = 3
