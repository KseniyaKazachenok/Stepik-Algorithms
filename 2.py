def count(n: int, k: int) -> int:
    """
    Считалка на вылет.

    :param n: Количество человек
    :param k: Количество слогов в считалке

    :return: Последний оставшийся человек
    """
    if n <= 0 or k <= 0:
        raise ValueError('Входные данные доолжны быть целыми положительными числами')

    people = []
    for i in range(1, n + 1):
        people.append(i)

    while len(people) > 1:
        if k > len(people):
            step = k % len(people)
            people.pop(step - 1)
        else:
            people.pop(k - 1)

    return people[0]


if __name__ == '__main__':
    c = count(5, 3)
    print(c)
