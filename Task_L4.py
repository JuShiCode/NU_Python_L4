# Домашнее задание:
# LIGHT:
#
# 1. Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка (могут повторяться,
# можно взять значения: количество имен 20, N = 100,
# рекомендуется использовать функцию random);

# Решение с помощью цикла
import random
names = ['Nancy', 'Alice', 'Mary', 'Hanna', 'Dolores', 'Brian', 'Stanley', 'Andrew', 'Michael', 'Nickolas', 'Johnathan', 'Angeline']
name_list = []
N = 1
for N in range(1,101):
    name_list.append(random.choice(names))
    N +=1
print(len(name_list), 'имён: ',name_list)

# Решение с помощью функции
import random
names = ['Nancy', 'Alice', 'Mary', 'Hanna', 'Dolores', 'Brian', 'Stanley', 'Andrew', 'Michael', 'Nickolas', 'Johnathan', 'Angeline']
N = 100
name_list = []
def F(N):
    if N >=1:
        name_list.append(random.choice(names))
        N -= 1
        return F(N)
    else:
        return name_list
print(f'{N} имён: {F(N)}')

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

# Решение с помощью цикла
names_dict = {}
for i in range(len(name_list)):
    names_dict[name_list[i]] = name_list.count(name_list[i])
top_names_list = list(names_dict.items())
top_names_list.sort(key = lambda i: i[1], reverse = True)
print(f'Имя {top_names_list[0][0]} встречается чаще других, а именно {top_names_list[0][1]} раз.')

# Решение с помощью функции
def top(name_list):
    common_name = dict((name_list.count(i), i) for i in set(name_list))
    return common_name[max(common_name.keys())]
print(f'Имя {top(name_list)} встречается чаще других, а именно {name_list.count(top(name_list))} раз.')

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
#  Решение с помощью цикла
letters_dict = {}
for i in range(len(name_list)):
    letters_dict[name_list[i][0]] = name_list.count(name_list[i])
letters_list = sorted(letters_dict.items(), key = lambda i: i[1])
# print(letters_list)
print('Первая буква', letters_list[0][0], 'в именах встречается реже других, а именно', letters_list[0][1], 'раз.')

# решение с помощью функции
letters_list = [name_list[i][0] for i in range(len(name_list))]
# print(letters_list)
def rare(letters_list):
    letters_dict = dict((letters_list[i], letters_list.count(letters_list[i])) for i in range(len(letters_list)))
    letters_dict_sort = sorted(letters_dict.items(), key = lambda i: i[1])
    return letters_dict_sort[0]
# print(rare(letters_list))
print(f'Первая буква {(rare(letters_list))[0]} в именах встречается реже других, а именно {(rare(letters_list))[1]} раз.')

# PRO:
# LIGHT +
#
# 4.  В файле с логами найти дату самого позднего лога (по метке времени):
# https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
#
log_file = open('log.txt', 'r', encoding = 'utf-8')
log_file_read = log_file.read()
print(log_file_read)
log_file_rows = log_file_read.split(sep='\n')
# print(log_file_rows)
data_list = []
for i in range(len(log_file_rows)):
    # print(i, log_file_rows[i][0:10])
    data_list.append(log_file_rows[i][0:10])
# print(data_list)
data_list.sort()
# print(data_list)
print('Дата последнего лога', data_list[-1])


log_file = open('log.txt', 'r', encoding = 'utf-8')
def last_log(log_file):
    log_file_read = log_file.read()
    log_file_rows = log_file_read.split(sep='\n')
    data_list = [log_file_rows[i][0:10] for i in range(len(log_file_rows))]
    data_list.sort()
    return (data_list[-1])
print('Дата последнего лога', last_log(log_file))