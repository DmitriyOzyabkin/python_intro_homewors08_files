'''
Задача 4. Частотный анализ
Есть файл text.txt, который содержит текст. Напишите программу, которая
выполняет частотный анализ, определяя долю каждой буквы английского
алфавита в общем количестве английских букв в тексте, и выводит результат в
файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
учитывать не нужно.
В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
тремя знаками в дробной части. Буквы должны быть отсортированы по
убыванию их доли. Буквы с равной долей должны следовать в алфавитном
порядке.
'''

from collections import Counter
from operator import itemgetter

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()[0].lower()

    char_count = Counter(text)
    letter_count = {}
    for key in char_count:
        if key.isalpha():
            letter_count[key] = char_count[key]

    total = sum(letter_count.values())

    for letter in letter_count:
        letter_count[letter] = round(letter_count[letter]/12, 3)

    d = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))
 
    for letter, freq in d:
        print(letter, freq)

