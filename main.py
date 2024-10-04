#import os
# # Создадим функцию для работы с заданными файлами
# def create_file_list(folder):
#     file_list = os.listdir(folder)  # Получаем список имен файлов в папке
#     merget_file_list = []  # Создаем список для хранения содержимого файлов
#     for file in file_list:
#         with open(folder + "/" + file) as _temp_file:  # Поочередно считываем файлы
#             # Добавляем в список название файла, значение для числа строк и список для содержимого файла
#             merget_file_list.append([file, 0, []])
#             for line in _temp_file:
#                 merget_file_list[-1][2].append(line.strip())  # Добавляем в список содержимое файла построчно
#                 merget_file_list[-1][1] += 1  # Увеличиваем значение для числа строк
#     # Возвращаем предварительно отсортированный по значению числа строк список с содержимым файлов
#     return sorted(merget_file_list, key=lambda x: x[1], reverse=False)
#
# #
# # Создадим функцию для записи итогового файла
# def create_merget_file(folder, filename):
#     with open(filename + '.txt', 'w+') as merget_file:  # Откроем (создадим) итоговый файл с именем "filename".txt
#         merget_file.write(f'Даны файлы:\n')
#         for file in create_file_list(folder):
#             merget_file.write(f'Назввание файла: {file[0]}\n')  # Записываем в итоговый файл имена начальных файлов
#             merget_file.write(f'Количество строк: {file[1]}\n')  # Записываем в итоговый файл число строк файлов
#             for string in file[2]:
#                 merget_file.write(string + '\n')  # Записываем в итоговый файл содержимое начальных файлов построчно
#             merget_file.write('\n')
#     return print('Файл создан')
#
#
# create_merget_file('txt', 'merget_file')

# with open('1.txt', 'r', encoding='utf-8') as file_1:
#     line_1 = {}
#     count_1 = 0
#     for line in file_1.readlines():
#         count_1 += 1
#         line_1['1.txt'] = count_1
# with open('1.txt', 'r', encoding='utf-8') as file_1:
#     text_1 = file_1.read()
#
# with open('2.txt', 'r', encoding='utf-8') as file_2:
#     line_2 = {}
#     count_2 = 0
#     for line in file_2.readlines():
#         count_2 += 1
#         line_2['2.txt'] = count_2
# with open('2.txt', 'r', encoding='utf-8') as file_2:
#     text_2 = file_2.read()
#
# with open('3.txt', 'r', encoding='utf-8') as file_3:
#     line_3 = {}
#     count_3 = 0
#     for line in file_3.readlines():
#         count_3 += 1
#         line_3['3.txt'] = count_3
# with open('3.txt', 'r', encoding='utf-8') as file_3:
#     text_3 = file_3.read()
#
# join = sorted(list(line_1.items()) + list(line_2.items()) + list(line_3.items()), key=lambda x: x[1])
#
# with open('result.txt', 'w', encoding='utf-8') as file_result:
#     for line in join:
#         file_result.write(f'{join[0][0]}\n {join[0][1]}\n {text_2}\n {join[1][0]}\n {join[1][1]}\n {text_1}\n{join[2][0]}\n{join[2][1]}\n {text_3}\n')

import os


def sort_files():
    files = os.listdir('sorted')
    result = []
    for file_ in files:
        with open(f'sorted/{file_}', 'r', encoding='utf8') as f:
            text = f.read()
            f.seek(0)
            result.append({'name': file_, 'count_lines': len(f.readlines()), 'text': text})

    sorted_files = sorted(result, key=lambda f: f['count_lines'])
    with open('result.txt', 'w', encoding='utf8') as f:
        for file_ in sorted_files:
            f.write(file_['name']+'\n')
            f.write(str(file_['count_lines'])+'\n')
            f.write(file_['text']+'\n')


sort_files()