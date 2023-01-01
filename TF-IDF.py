import collections

def spisok(text):
  l = []
  for i in text:
    l.append(i)
  return l

text_1 = 'Матушка была еще мною брюхата, как уже я был записан в Семеновский полк сержантом, по милости майора гвардии князя В., близкого нашего родственника. Если бы паче всякого чаяния матушка родила дочь, то батюшка объявил бы куда следовало о смерти неявившегося сержанта, и дело тем бы и кончилось. Я считался в отпуску до окончания наук. В то время воспитывались мы не по-нонешнему. С пятилетнего возраста отдан я был на руки стремянному Савельичу, за трезвое поведение пожалованному мне в дядьки. Под его надзором на двенадцатом году выучился я русской грамоте и мог очень здраво судить о свойствах борзого кобеля. В это время батюшка нанял для меня француза, мосье Бопре, которого выписали из Москвы вместе с годовым запасом вина и прованского масла. Приезд его сильно не понравился Савельичу'.split()
text_2 = 'Однажды осенью матушка варила в гостиной медовое варенье, а я, облизываясь, смотрел на кипучие пенки. Батюшка у окна читал Придворный календарь, ежегодно им получаемый. Эта книга имела всегда сильное на него влияние: никогда не перечитывал он ее без особенного участия, и чтение это производило в нем всегда удивительное волнение желчи. Матушка, знавшая наизусть все его свычаи и обычаи, всегда старалась засунуть несчастную книгу как можно подалее, и таким образом Придворный календарь не попадался ему на глаза иногда по целым месяцам. Зато, когда он случайно его находил, то, бывало, по целым часам не выпускал уж из своих рук. Итак, батюшка читал Придворный календарь, изредка пожимая плечами и повторяя вполголоса: «Генерал-поручик!.. Он у меня в роте был сержантом!.. Обоих российских орденов кавалер!.. А давно ли мы...» Наконец батюшка швырнул календарь на диван и погрузился в задумчивость, не предвещавшую ничего доброго'.split()
text_3 = 'Матушка отыскала мой паспорт, хранившийся в ее шкатулке вместе с сорочкою, в которой меня крестили, и вручила его батюшке дрожащею рукою. Батюшка прочел его со вниманием, положил перед собою на стол и начал свое письмо'.split()

print(spisok(text_1))
print ('----------------------------------------------')
print(spisok(text_2))
print ('----------------------------------------------')
print(spisok(text_3))
print ('----------------------------------------------')

def compute_tf(text):
#На вход берем текст в виде списка (list) слов
    #Считаем частотность всех терминов во входном массиве с помощью 
    #метода Counter библиотеки collections
    tf_text = collections.Counter(text)
    for i in tf_text:
        #для каждого слова в tf_text считаем TF путём деления
        #встречаемости слова на общее количество слов в тексте
        tf_text[i] = tf_text[i]/float(len(text))
    #возвращаем объект типа Counter c TF всех слов текста
    return tf_text

print (compute_tf(text_1))
print ('----------------------------------------------')
print (compute_tf(text_2))
print ('----------------------------------------------')
print (compute_tf(text_3))


import math

def compute_idf(word, corpus):
#на вход берется слово, для которого считаем IDF
#и корпус документов в виде списка списков слов
        #количество документов, где встречается искомый термин
        #считается как генератор списков
        return math.log1p(len(corpus)/sum([1.0 for i in corpus if word in i]))
        
texts = [['Матушка', 'была', 'еще', 'мною', 'брюхата,', 'как', 'уже', 'я', 'был', 'записан', 'в', 'Семеновский', 'полк', 'сержантом,', 'по', 'милости', 'майора', 'гвардии', 'князя', 'В.,', 'близкого', 'нашего', 'родственника.', 'Если', 'бы', 'паче', 'всякого', 'чаяния', 'матушка', 'родила', 'дочь,', 'то', 'батюшка', 'объявил', 'бы', 'куда', 'следовало', 'о', 'смерти', 'неявившегося', 'сержанта,', 'и', 'дело', 'тем', 'бы', 'и', 'кончилось.', 'Я', 'считался', 'в', 'отпуску', 'до', 'окончания', 'наук.', 'В', 'то', 'время', 'воспитывались', 'мы', 'не', 'по-нонешнему.', 'С', 'пятилетнего', 'возраста', 'отдан', 'я', 'был', 'на', 'руки', 'стремянному', 'Савельичу,', 'за', 'трезвое', 'поведение', 'пожалованному', 'мне', 'в', 'дядьки.', 'Под', 'его', 'надзором', 'на', 'двенадцатом', 'году', 'выучился', 'я', 'русской', 'грамоте', 'и', 'мог', 'очень', 'здраво', 'судить', 'о', 'свойствах', 'борзого', 'кобеля.', 'В', 'это', 'время', 'батюшка', 'нанял', 'для', 'меня', 'француза,', 'мосье', 'Бопре,', 'которого', 'выписали', 'из', 'Москвы', 'вместе', 'с', 'годовым', 'запасом', 'вина', 'и', 'прованского', 'масла.', 'Приезд', 'его', 'сильно', 'не', 'понравился', 'Савельичу'], ['Однажды', 'осенью', 'матушка', 'варила', 'в', 'гостиной', 'медовое', 'варенье,', 'а', 'я,', 'облизываясь,', 'смотрел', 'на', 'кипучие', 'пенки.', 'Батюшка', 'у', 'окна', 'читал', 'Придворный', 'календарь,', 'ежегодно', 'им', 'получаемый.', 'Эта', 'книга', 'имела', 'всегда', 'сильное', 'на', 'него', 'влияние:', 'никогда', 'не', 'перечитывал', 'он', 'ее', 'без', 'особенного', 'участия,', 'и', 'чтение', 'это', 'производило', 'в', 'нем', 'всегда', 'удивительное', 'волнение', 'желчи.', 'Матушка,', 'знавшая', 'наизусть', 'все', 'его', 'свычаи', 'и', 'обычаи,', 'всегда', 'старалась', 'засунуть', 'несчастную', 'книгу', 'как', 'можно', 'подалее,', 'и', 'таким', 'образом', 'Придворный', 'календарь', 'не', 'попадался', 'ему', 'на', 'глаза', 'иногда', 'по', 'целым', 'месяцам.', 'Зато,', 'когда', 'он', 'случайно', 'его', 'находил,', 'то,', 'бывало,', 'по', 'целым', 'часам', 'не', 'выпускал', 'уж', 'из', 'своих', 'рук.', 'Итак,', 'батюшка', 'читал', 'Придворный', 'календарь,', 'изредка', 'пожимая', 'плечами', 'и', 'повторяя', 'вполголоса:', '«Генерал-поручик!..', 'Он', 'у', 'меня', 'в', 'роте', 'был', 'сержантом!..', 'Обоих', 'российских', 'орденов', 'кавалер!..', 'А', 'давно', 'ли', 'мы...»', 'Наконец', 'батюшка', 'швырнул', 'календарь', 'на', 'диван', 'и', 'погрузился', 'в', 'задумчивость,', 'не', 'предвещавшую', 'ничего', 'доброго'], ['Матушка', 'отыскала', 'мой', 'паспорт,', 'хранившийся', 'в', 'ее', 'шкатулке', 'вместе', 'с', 'сорочкою,', 'в', 'которой', 'меня', 'крестили,', 'и', 'вручила', 'его', 'батюшке', 'дрожащею', 'рукою.', 'Батюшка', 'прочел', 'его', 'со', 'вниманием,', 'положил', 'перед', 'собою', 'на', 'стол', 'и', 'начал', 'свое', 'письмо']]
print (compute_idf('матушка', texts))

from collections import Counter
import math

def compute_tfidf(corpus):

  def compute_tf(text):

    tf_text = Counter(text)

    for i in tf_text:

      tf_text[i] = tf_text[i]/float(len(text))

    return tf_text

  def compute_idf(word, corpus):

    return math.log1p(len(corpus)/sum([1.0 for i in corpus if word in i]))


  documents_list = []

  for text in corpus:

    tf_idf_dictionary = {}

    computed_tf = compute_tf(text)
    
    for word in computed_tf:

      tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)

    documents_list.append(tf_idf_dictionary)

  return documents_list

corpus = [['Матушка', 'была', 'еще', 'мною', 'брюхата,', 'как', 'уже', 'я', 'был', 'записан', 'в', 'Семеновский', 'полк', 'сержантом,', 'по', 'милости', 'майора', 'гвардии', 'князя', 'В.,', 'близкого', 'нашего', 'родственника.', 'Если', 'бы', 'паче', 'всякого', 'чаяния', 'матушка', 'родила', 'дочь,', 'то', 'батюшка', 'объявил', 'бы', 'куда', 'следовало', 'о', 'смерти', 'неявившегося', 'сержанта,', 'и', 'дело', 'тем', 'бы', 'и', 'кончилось.', 'Я', 'считался', 'в', 'отпуску', 'до', 'окончания', 'наук.', 'В', 'то', 'время', 'воспитывались', 'мы', 'не', 'по-нонешнему.', 'С', 'пятилетнего', 'возраста', 'отдан', 'я', 'был', 'на', 'руки', 'стремянному', 'Савельичу,', 'за', 'трезвое', 'поведение', 'пожалованному', 'мне', 'в', 'дядьки.', 'Под', 'его', 'надзором', 'на', 'двенадцатом', 'году', 'выучился', 'я', 'русской', 'грамоте', 'и', 'мог', 'очень', 'здраво', 'судить', 'о', 'свойствах', 'борзого', 'кобеля.', 'В', 'это', 'время', 'батюшка', 'нанял', 'для', 'меня', 'француза,', 'мосье', 'Бопре,', 'которого', 'выписали', 'из', 'Москвы', 'вместе', 'с', 'годовым', 'запасом', 'вина', 'и', 'прованского', 'масла.', 'Приезд', 'его', 'сильно', 'не', 'понравился', 'Савельичу'], ['Однажды', 'осенью', 'матушка', 'варила', 'в', 'гостиной', 'медовое', 'варенье,', 'а', 'я,', 'облизываясь,', 'смотрел', 'на', 'кипучие', 'пенки.', 'Батюшка', 'у', 'окна', 'читал', 'Придворный', 'календарь,', 'ежегодно', 'им', 'получаемый.', 'Эта', 'книга', 'имела', 'всегда', 'сильное', 'на', 'него', 'влияние:', 'никогда', 'не', 'перечитывал', 'он', 'ее', 'без', 'особенного', 'участия,', 'и', 'чтение', 'это', 'производило', 'в', 'нем', 'всегда', 'удивительное', 'волнение', 'желчи.', 'Матушка,', 'знавшая', 'наизусть', 'все', 'его', 'свычаи', 'и', 'обычаи,', 'всегда', 'старалась', 'засунуть', 'несчастную', 'книгу', 'как', 'можно', 'подалее,', 'и', 'таким', 'образом', 'Придворный', 'календарь', 'не', 'попадался', 'ему', 'на', 'глаза', 'иногда', 'по', 'целым', 'месяцам.', 'Зато,', 'когда', 'он', 'случайно', 'его', 'находил,', 'то,', 'бывало,', 'по', 'целым', 'часам', 'не', 'выпускал', 'уж', 'из', 'своих', 'рук.', 'Итак,', 'батюшка', 'читал', 'Придворный', 'календарь,', 'изредка', 'пожимая', 'плечами', 'и', 'повторяя', 'вполголоса:', '«Генерал-поручик!..', 'Он', 'у', 'меня', 'в', 'роте', 'был', 'сержантом!..', 'Обоих', 'российских', 'орденов', 'кавалер!..', 'А', 'давно', 'ли', 'мы...»', 'Наконец', 'батюшка', 'швырнул', 'календарь', 'на', 'диван', 'и', 'погрузился', 'в', 'задумчивость,', 'не', 'предвещавшую', 'ничего', 'доброго'], ['Матушка', 'отыскала', 'мой', 'паспорт,', 'хранившийся', 'в', 'ее', 'шкатулке', 'вместе', 'с', 'сорочкою,', 'в', 'которой', 'меня', 'крестили,', 'и', 'вручила', 'его', 'батюшке', 'дрожащею', 'рукою.', 'Батюшка', 'прочел', 'его', 'со', 'вниманием,', 'положил', 'перед', 'собою', 'на', 'стол', 'и', 'начал', 'свое', 'письмо']]
print (compute_tfidf(corpus))