import array_operations as arr
from typing import List


def insert_sort(array: List):
    len_array = len(array)
    for i in range(0, len_array):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp
            elif array[j] > array[j - 1] and j == len_array - 1:
                break

    return array


if __name__ == '__main__':
    A = arr.arr_create_rand(50)
    print(A)
    print(insert_sort(A))
