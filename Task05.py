'''Задача 5*. «Война и мир»
Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это
довольно объёмное произведение лежит в архиве voina-i-mir.zip. Напишите
программу, которая подсчитывает статистику по буквам (не только русского
алфавита) в этом романе и выводит результат на экран (или в файл). Результат
должен быть отсортирован по частоте встречаемости букв (по возрастанию или
убыванию). Регистр символов имеет значение.'''

from collections import Counter

with open('voyna-i-mir.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    char_count = Counter(text)

# sorted(char_count, )

print(char_count)

with open('VIM_letter_count.txt', 'w', encoding='utf-8') as file:
    for key, value in sorted(char_count.items(), key=lambda item: item[1], reverse=True):
        if key.isalpha():
            file.write(f"'{key}' occurs  {value} times\n")

