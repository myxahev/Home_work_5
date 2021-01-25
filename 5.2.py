# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('out_file.txt') as file:
    print(sum(1 for line in file))

    print(len(file.read()))
