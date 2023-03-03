def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError('Нельзя определить факториал отрицательного числа')

    if not isinstance(n, int):
        raise TypeError('Факториал определяется только для целых чисел')

    if n == 0:
        return 1

    return factorial_recursive(n - 1) * n
