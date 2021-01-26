# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('out_file.txt', 'w', encoding='utf-8') as file_object:
    while True:
        print('Введите данные и нажмите enter, по окончании введите пустую строку')
        user_answer = input('Введите данные:')
        file_object.writelines(user_answer + '\n')
        if user_answer == '':
            print('Выход из программы')
            break