from random import randint
import time  # измеряем время, необходимое для выполнения скрипта этой штукой
start_time = time.time()

'''* Создать большой массив из 1_000_000 элеиментов с отсортированными числами.
Массив генерируется случайным образом.
* Написать функцию, которая находит индекс элемента def find_idx(mass, target),
если элемент присутствует , иначе возвращается 'Number is not in array'.
* Померить сколько милисекунд ваша функция выполняется для какого-то значения
из массива с помощью 'import time'.'''

N = 10
mass = []
target = int(input('Ввести целое число: '))


def find_index(mass, target):
    for i in range(N):
        mass.append(randint(1, 10))
        mass.sort()
        if target in mass[:target]:
            indx_target = mass.index(target)
            return 'Index: ', indx_target
# Если оставить else включенным, то будет писать столько раз, сколько чисел не в массиве.
#        else:
#            print('Number is not in array')
    print("--- %s seconds ---" % (time.time() - start_time))
find_index(mass, target)

#А вот так работает ОК, но это без def, а надо с def

for i in range(N):
    mass.append(randint(1, 100))
    array_sorted = sorted(mass)
print(array_sorted)

if target in mass[:target]:
    indx_target = mass.index(target)
    print(indx_target)
else:
    print('Number is not in array')
print("--- %s seconds ---" % (time.time() - start_time))
