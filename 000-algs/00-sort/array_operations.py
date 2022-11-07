from typing import List


def arr_create(count_of_elements: int):
    array = []
    for i in range(5):
        array.append(i)

    return array


def arr_reverse(array: List):
    """Инверитирует элементы массива

    :param array: List
    :return: List - invert array
    """
    len_array = len(array)
    tmp_array = [0] * len_array
    for i in range(len_array):
        tmp_array[i] = array[len_array - 1 - i]
    return tmp_array


def arr_change(array: List, a: int, index: int):
    """Меняем произвольный элемент массива

    :param array: List - Изменяемый массив
    :param a: int - Новые данные
    :param index: int - Какой элемент меняем
    :return: List
    """
    array[index] = a
    return array


def arr_turn(array: List, ind_frst: int, ind_scnd: int):
    """Меняем местами произвольные элементы

    :param array: List - Изменяемый массив
    :param ind_frst: int - Индекс первого элемента из пары меняемых значений
    :param ind_scnd: int - Индекс второго элемента из пары меняемых значений
    :return: List
    """
    tmp_var = array[ind_frst]
    array[ind_frst] = array[ind_scnd]
    array[ind_scnd] = tmp_var

    return array


def arr_shift_l(array: List):
    i = 0
    while i <= len(array) - 1:
        if i == len(array) - 1:
            array[i] = 0
        else:
            array[i] = array[i + 1]

        i += 1

    return array


def arr_shift_r(array: List):
    # array = arr_reverse(array)
    # array.append(0)
    # array = arr_reverse(array)
    # array.pop()
    # return array

    len_array = len(array)
    tmp_array = [0] * len_array
    for i in range(len_array - 1):
        tmp_array[i + 1] = array[i]

    return tmp_array


def arr_insert(array: List, a: int, index: int):
    """Вставка нового элемента в произвольное место

    :param array: List - Изменяемый массив
    :param a: int - Новые данные
    :param index: int - Индекс нового элемента
    :return: List
    """
    # len_array = len(array)
    # tmp_array = [0]*(len_array+1)
    # for i in range(len_array+1):
    #     if i < index:
    #         tmp_array[i] = array[i]
    #     elif i == index:
    #         tmp_array[i] = a
    #     else:
    #         tmp_array[i] = array[i - 1]
    #
    # return tmp_array

    array.append(0)
    len_array = len(array)
    for i in range(len_array - 1, index-1, -1):
        array[i] = array[i - 1]

    array[index] = a

    return array


A = arr_create(5)

# print(arr_reverse(A))
# print(arr_change(A, 100, 3))
# print(arr_turn(A, 1, 3))
# print(arr_shift_l(A))

print(arr_insert(A, 100, 2))

# B = arr_create(5)
# print(arr_shift_r(B))
