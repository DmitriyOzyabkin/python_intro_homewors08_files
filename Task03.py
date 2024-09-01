'''
Задача 3. Турнир
В файле first_tour.txt записано число K и данные об участниках турнира по
настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
первом туре. Во второй тур проходят участники, которые набрали более K
баллов в первом туре.
Напишите программу, которая выводит в файл second_tour.txt данные всех
участников, прошедших во второй тур, с нумерацией.
В первой строке нужно вывести в файл second_tour.txt количество участников
второго тура. Затем программа должна вывести фамилии, инициалы и
количество баллов всех участников, прошедших во второй тур, с нумерацией.
Имя нужно сократить до одной буквы. Список должен быть отсортирован по
убыванию набранных баллов.
'''
with open('first_tour.txt', 'r', encoding='utf-8') as file:
    first_tour = file.readlines()
    min_score = int(first_tour[0])
    second_tour = []

    for person in first_tour[1:]:
        pers_score = person.split()
        if int(pers_score[2]) > min_score:
            second_tour.append((pers_score[1][0]+'.' + ' ' + pers_score[0], int(pers_score[2])))

    sorted_second_tour = sorted(second_tour, key=lambda item: item[1], reverse=True)

with open('second_tour.txt', 'w', encoding='utf-8') as file:
    file.write(str(len(sorted_second_tour))+'\n')
    for i in range(len(sorted_second_tour)):
        file.write(f'{i+1}) {sorted_second_tour[i][0]} {sorted_second_tour[i][1]}'+'\n')
