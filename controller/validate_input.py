def flight_num_input(prompt) -> str:
    """
    Проверка корректности ввода номера рейса пользователем.
    :param prompt: Ввод пользователя.
    :return: Возврат номера после проверки.
    """
    while True:
        try:
            if len(prompt) != 4:
                raise ValueError
            break
        except ValueError:
            print('Неверный формат номера рейса!')
            prompt = input('XXXХ - номер рейса: ').upper()

    return prompt


def cmd_input(commands_dict, prompt) -> int:
    """
    Проверка корректности ввода номера команды пользователем (типа данных, наличие команды в списке команд).
    :param commands_dict: Словарь команд
    :param prompt: Ввод пользователя.
    :return: Номер команды.
    """
    while True:
        try:
            prompt = int(prompt)
            if prompt not in commands_dict:
                raise KeyError
            break
        except ValueError:
            print('Неверный ввод пункта меню!')
        except KeyError:
            print('Команда отсутствует!')

        prompt = input('\nВведите номер пункта меню: ')

    return prompt


def date_input(prompt) -> str:
    """
    Проверка формата ввода даты вылета пользователем.
    :param prompt: Ввод пользователя.
    :return: Дата.
    """
    while True:
        try:
            if len(prompt) != 10:
                raise ValueError
            if prompt[2] not in ['.', '/'] or prompt[5] not in ['.', '/']:
                raise SyntaxError
            if int(prompt[0:2]) > 31 or int(prompt[3:5]) > 12:
                raise ValueError
            break
        except ValueError or SyntaxError:
            print('Неверный формат даты (ДД/ММ/ГГГГ)!')
            prompt = input('ДД/ММ/ГГГГ - дата рейса: ').upper().strip()

    return prompt


def time_input(prompt) -> str:
    """
    Проверка формата ввода времени вылета пользователем.
    :param prompt: Ввод пользователя.
    :return: Время.
    """
    while True:
        try:
            if len(prompt) != 5:
                raise ValueError
            if prompt[2] not in [':']:
                raise SyntaxError
            if int(prompt[0:2]) > 24 or int(prompt[3:5]) > 59:
                raise ValueError
            break
        except ValueError or SyntaxError:
            print('Неверный формат времени (ЧЧ:ММ)!')
            prompt = input('ЧЧ:ММ - время вылета: ').upper().strip()

    return prompt


def flight_duration_input(prompt) -> str:
    """
    Проверка формата ввода продолжительности полета пользователем.
    :param prompt: Ввод пользователя.
    :return: Продолжительность полета.
    """
    while True:
        try:
            if len(prompt) != 5:
                raise ValueError
            if prompt[2] not in ['.']:
                raise SyntaxError
            break
        except ValueError or SyntaxError:
            print('Неверный формат времени (ЧЧ.ММ)!')
            prompt = input('ЧЧ.ММ - длительность полёта: ').upper().strip()

    return prompt


def airport_code_input(prompt) -> str:
    """
    Проверка формата ввода пользователем кода аэропорта.
    :param prompt: Ввод пользователя.
    :return: Код аэропорта.
    """
    literal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    while True:
        try:
            if len(prompt) != 3:
                raise ValueError
            for _ in prompt:
                if _.upper() not in literal:
                    raise SyntaxError
            break
        except ValueError or SyntaxError:
            print('Неверный формат кода аэропорта (ХХХ)!')
            prompt = input('XXX - аэропорт вылета: ').upper().strip()

    return prompt


def ticket_price_input(prompt) -> float:
    """
    Проверка корректности ввода пользователем цены билета.
    :param prompt: Ввод пользователя.
    :return: Цена билета.
    """
    while True:
        new_prompt = ''
        try:
            for _ in prompt:
                if _ == ',':
                    new_prompt += '.'
                else:
                    new_prompt += _
            new_prompt = float(new_prompt)
            if new_prompt < 0:
                raise ValueError
            break
        except ValueError:
            print('Неверный формат стоимости билета (.ХХ)!')
            prompt = input('.XX - стоимость билета: ').upper().strip()

    return new_prompt
