def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """

    brackets_char = ["(", "{", "["]
    brackets_stack = []

    for char in brackets_row:
        if char in brackets_char:
            brackets_stack.append(char)
        else:
            if not brackets_stack:
                return False

            current_char = brackets_stack.pop()

            if current_char == '(':
                if char != ')':
                    return False

            if current_char == '{':
                if char != '}':
                    return False

            if current_char == '[':
                if char != ']':
                    return False

    if brackets_stack:
        return False
    return True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
