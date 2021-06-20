"""
* Создать большой массив из N = 1_000_000 элеиментов с отсортированными числами.
Массив генерируется случайным образом.
* Написать функцию, которая находит индекс элемента def find_idx(mass, target),
если элемент присутствует , иначе возвращается 'Number is not in array'.
* Померить сколько милисекунд ваша функция выполняется для какого-то значения
из массива с помощью 'import time'.
"""

from random import randint
# измеряем время, необходимое для выполнения скрипта
import time

start_time = time.time()

# Количество элементов массива
N = 1_000_000

array_random = sorted([randint(1, N) for _ in range(N)])

# Число, индекс которого необходимо найти в массиве
target = int(input('Ввести целое число: '))


def find_index(array_random, target):
    try:
        return 'Index: ', array_random.index(target)
    except ValueError:
        return 'Number is not in array'


print(find_index(array_random, target))
print("--- %s seconds ---" % (time.time() - start_time))
