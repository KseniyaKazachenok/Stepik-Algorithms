def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError('Нельзя определить факториал отрицательного числа')

    if not isinstance(n, int):
        raise TypeError('Факториал определяется только для целых чисел')

    if n == 0:
        return 1

    fact_ = 1
    while n > 1:
        fact_ *= n
        n -= 1
    return fact_
