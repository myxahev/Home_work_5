# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


with open('out_file.txt') as f:
    count_lines = len(f.readlines())
    f.seek(0)

    num_line = 0
    while True:
        num_line += 1
        line = len(f.readline().split())
        print(f'В {num_line} строке {line} слово')
        if line == 0 or num_line == count_lines:
            break
    print(f'Общее количество строк: {count_lines - 1}')