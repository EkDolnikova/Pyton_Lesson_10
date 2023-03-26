"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

my_list = ['разработка', 'сокет', 'декоратор']
for el in my_list:
    print(f'тип переменной: {type(el)}, содержание:  {el}')

for el in my_list:
    a = el.encode('unicode_escape').decode('utf-8')
    print(f'тип переменной: {type(a)}, содержание:  {a}')
