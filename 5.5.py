# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


with open('5.5.txt', 'w') as f:

    f.write('1 22 333 4444 55555 666666 7777777 888888888 999999999')

with open('5.5.txt') as file_object:
    a = file_object.readline().split()
    result = sum([int(item) for item in a])
    print(result)