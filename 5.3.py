# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('5.3.txt', encoding='utf-8') as f:
    count_lines = len(f.readlines())
    f.seek(0)
    users = []
    line = 0
    i = 1
    while True:
        line += 1
        user = f.readline().split()
        user[i] = float(user[i])
        users.append(user)
        if line == count_lines:
            all_users = dict(users)
            break
    salary = []
    for key, value in all_users.items():
        if value <= 20000:
            salary.append(key)

print('Оклад меньше 20000 у:', salary)
print('Средний оклад у сотрудников: ', round(sum(list(all_users.values()))) / count_lines)


