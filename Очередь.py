"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Первый элемент - начало очереди
        Последний элемент - конец очереди
        """

        self._queue = list()
        self.len = 0

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемента в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """

        self._queue.append(elem)
        self.len += 1

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """

        if not self._queue:
            raise IndexError('Очередь пуста')

        self.len -= 1
        return self._queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала,
        0 - первый с начала элемент в очереди,
        1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """

        if not isinstance(ind, int):
            raise TypeError('Индекс должен быть целым числом')

        if not 0 <= ind <= len(self):
            raise IndexError('Индекс вне границ стека')

        return self._queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """

        self._queue.clear()
        self.len = 0

    def __len__(self):
        """ Количество элементов в очереди. """

        return self.len


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    print(queue.peek())
