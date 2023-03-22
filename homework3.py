# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны
#
# Необходимо объединить их в один по следующим правилам:
#
# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым
# нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем



# Пример Даны файлы: 1.txt
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
#
# 2.txt
# Строка номер 1 файла номер 2

#Итоговый файл:
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

import os.path

def read_file():
    list_files = ['1.txt', '2.txt', '3.txt']
    str_files = []
    for file in list_files:
        with open(file, 'r', encoding='utf-8') as f:
            temp = []
            for line in f:
                temp.append(line.strip())
            temp.insert(0, str(len(temp)))
            temp.insert(0, file)
            str_files.append(temp)
    str_files.sort(key=len)

    file = 'TEXT.txt'
    with open(file, 'w', encoding='utf-8') as f:
        for string in str_files:
            for i in string:
                f.writelines(i + '\n')
    return

print(read_file())

