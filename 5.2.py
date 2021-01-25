# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

print(sum(1 for line in open('out_file.txt', 'r')))

print(len(open('out_file.txt', 'r').read()))