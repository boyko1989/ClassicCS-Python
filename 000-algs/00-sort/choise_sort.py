from typing import List
import array_operations as arr


def choise_sort(array: List):
    """Сортировка выбором
    1. Сравниваем текущий элемент с предыдущим
        - Если тек
    """
    len_array = len(array)
    min = 0
    for i in range(len_array):
        if array[min] > array[i]:
            min = i

    return array


if __name__ == '__main__':
    A = arr.arr_create_rand(5)
    print(A)
    choise_sort(A)