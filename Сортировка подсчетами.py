from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container

    counts = [0 for value in range(max(container) + 1)]

    for value in container:
        counts[value] += 1

    for index in range(1, len(counts)):
        counts[index] = counts[index - 1] + counts[index]

    container_sorted = [0 for value in range(len(container))]

    for value in container:
        index = counts[value] - 1
        container_sorted[index] = value
        counts[value] -= 1

    return container_sorted
