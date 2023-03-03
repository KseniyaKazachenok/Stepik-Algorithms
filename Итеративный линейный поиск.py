"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError('Пустая последовательность')
    min_ = arr[0]

    for ind, value in enumerate(arr):
        for val in arr:
            if val < min_:
                min_ = val
        if value == min_:
            return ind
