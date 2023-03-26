import re


def dna_str(n: int, m: int) -> str:
    """
    Построение консенсус-строки для DNA рядов.

    :param n: Количество DNA рядов
    :param m: Количество букв в одном ряду

    :return: консенсус-строка
    """
    re_str = '[ACGT]{%d}' % m
    str_list = []
    while n > 0:
        val = input('Введите строку ')
        if bool(re.fullmatch(re_str, val)) is False:
            print(f"Значение должно быть длиной {m} символа из списка {['A', 'C', 'G', 'T']}")
        elif bool(re.fullmatch(re_str, val)) is True:
            list_val = []
            for i in val:
                list_val.append(i)
            str_list.append(list_val)
            n -= 1
            continue
        else:
            break

    dna_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    result = []

    for i in range(len(str_list[0])):
        for j in str_list:
            if j[i] == "A":
                dna_dict['A'] += 1
            elif j[i] == "C":
                dna_dict['C'] += 1
            elif j[i] == "G":
                dna_dict['G'] += 1
            elif j[i] == "T":
                dna_dict['T'] += 1
        sorted_dna = sorted(dna_dict.items(), key=lambda x: x[1])
        result.append(sorted_dna[-1])
        dna_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    str_result = []
    for i in result:
        str_result.append(i[0])

    str_dna = ''.join(str_result)

    return str_dna


if __name__ == '__main__':
    print(dna_str(4, 4))
