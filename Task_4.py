"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

my_list = ['разработка', 'администрирование', 'protocol', 'standard']

for el in my_list:
    my_byte = el.encode('utf-8')
    print(f'тип переменной: {type(my_byte)}, содержание:  {my_byte}')

    my_str = bytes.decode(my_byte, 'utf-8')
    print(f'тип переменной: {type(my_str)}, содержание:  {my_str}')

