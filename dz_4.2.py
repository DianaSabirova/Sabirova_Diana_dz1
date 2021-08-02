#2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
#и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
#В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
#Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
#Можно ли, используя только методы класса str, решить поставленную задачу?
#Функция должна возвращать результат числового типа, например float.
#Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
#Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None.
#Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
#В качестве примера выведите курсы доллара и евро.
from requests import get, utils

# так как информация в бинарном виде, то записываем этот код в одну строку вместо двух
response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

#encodings=utils.get_encoding_from_headers(response.headers)
#content =response.content.decode(encoding=encodings)

def currency_rates(code):
    content = (response.split("<Valute ID="))# первый блок это дата ['<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="31.07.2021" name="Foreign Currency Market">
    # второй блок это уже информация по валютам <Valute ID="R01010"><NumCode..
    for i in content: # content-переменная, которую я отфильтровала чтобы перебрать значения начинающиеся с Value ID=
    #для того чтобы валюта каждой страны была в столбике
        if code.upper() in i: # в коде именно валюта имеет только большие буквы, поэтому мы будем работать только с ним
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", ".")) # и когда он находит значения начинающие с большой буквы, то преступает к этим действиям:
        #он убирает "/" и делает сплит по "<Value>", нам нужно значение второе с конца [-2]
print(currency_rates("USD"))








