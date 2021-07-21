#5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
#nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#        Например:
#>>> get_jokes(2)
#["лес завтра зеленый", "город вчера веселый"]
#Документировать код функции.
#Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choice, randrange

nouns = ["зебра", "яхта", "земля", "лягушка", "лилия"] # вормируем список из существительных. Я сформировала список из имен женского рода, чтобы не было синтаксической ошибки
time = ["сегодня","завтра","послезавтра","вчера","позавчера", "днём", "вечером", "ночью", "в сумерки",'когда-то'] # время в которое будет происходить действие над кем-то
adjectives = ["задорная","радостная","глупая","унылая","утонченная","яркая"] #прилагательные



def get_jokes(g, repeat = False) #создаем функцию и присваиваем ей аргументы с которыми мы будем работать


    """

Функция возвращает уникальные шутки, созданные случайно из 3-х списков
Выбираем только уникальные шутки. Чтобы они не повторялись.
Для этого подойдет метод .repeat-уникальный
quantity - кол-во элементов на повторении

    """


    # копируем списки, чтобы работать с копиями. Так как будем работать с удалениями pop
no = nouns.copy() # копия существительных
t = time.copy() # копия разных времен
adj = adjectives.copy() # копия прилагательных
list_of_jokes = [] # создаем пустой список
list_min = min(no, t, adj) # находим список содержащий минимальное кол-во символов


#цикл while должен работать пока есть кол-во эл-ов на повторении
# и длина равна минимальному списку
while g and len(list_min):# пока оба значения истины
# мы присваиваем переменной num значение равное, случайному  - randrange.
# Это случайное значение должно не выходить за рамки минимального кол-ва элементов из списков.
#Их должно быть определенное кол-во
    num = randrange(len(list_min))
    if repeat: # если значения повторяются, то нужно удалить их.
        list_of_jokes.append(f"{no.pop(num)} {f.pop(num)} {{adj.pop(num)})")  # сущ + время + прил

    else: # если повторений нет, то мы уже берем не копии, а настоящий список и форматируем(прибавляем) наши значения

        #choice - случайное слово из списка
        list_of_jokes.append(f"{choice(nouns)} {choice(time)} {choice(adjectives)}")
    q -= 1 #
return list_of_jokes
print(get_jokes(10, True))

# я не совсем понимаю, где ошибка. А также почему мы используем метод .pop? Ведь pop работает с индексами













