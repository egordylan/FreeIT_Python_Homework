'''* Создать большой массив из N = 1_000_000 элеиментов с отсортированными числами.
Массив генерируется случайным образом.
* Написать функцию, которая находит индекс элемента def find_idx(mass, target),
если элемент присутствует , иначе возвращается 'Number is not in array'.
* Померить сколько милисекунд ваша функция выполняется для какого-то значения
из массива с помощью 'import time'.'''

from random import randint
import time  # измеряем время, необходимое для выполнения скрипта этой штукой

start_time = time.time()

mass = []

target = int(input('Ввести целое число: '))  # Число, индекс которого необходимо найти в массиве

N = 1_000_000  # Количество элементов массива


def find_index(mass, target):
    counter = 0
    for i in range(N):
        mass.append(randint(1, 1_000_000))
        # Создан отсортированный массив случайных чисел
        mass.sort()
        if target not in mass:
            counter += 1
            print('puk')
            continue
        else:
            indx_target = mass.index(target)
            print('Our array', mass)
            return 'Index: ', indx_target
    if counter == N:
            print('Number is not in array')
print(find_index(mass, target))
print("--- %s seconds ---" % (time.time() - start_time))
