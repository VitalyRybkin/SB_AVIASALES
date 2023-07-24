from controller.validate_input import Validate as validate
from controller.flight import Flight
from controller.user_controller import UserController as controller


class RunService:
    """
    Пользовательский класс ввода вывода информации.
    """

    def __init__(self, cmd):
        self.__cmd = cmd
        self.flight = Flight
        self.controller = controller()
        self.validate = validate()

    @property
    def get_cmd(self):
        return self.__cmd

    def run_service(self):
        """
        Главная функция обработки информации и входящих команд.
        :return: Нет
        """
        print('Сервис поиска авиабилетов ... \n')
        self.controller.read_from_repo()

        while True:
            print('\nГлавное меню:\n')
            commands_exe = dict()
            commands_dict = dict()
            count = 1

            for k, v in self.get_cmd.items():
                if not k == 'exit':
                    try:
                        commands_exe[count] = eval('self.' + k)
                    except AttributeError:
                        print('Execution error: function "{}" not found!\n'.format(k))
                    commands_dict[count] = v
                    count += 1
                else:
                    commands_exe[0] = eval(k)
                    commands_dict[0] = v

            print('\n'.join('{}: {}'.format(k, v) for k, v in commands_dict.items()))

            cmd_input = input('\nВведите номер пункта меню: ')
            cmd_input = self.validate.cmd_input(commands_dict, cmd_input)

            if cmd_input == 0:
                self.controller.save_to_repo()
                commands_exe.get(cmd_input)()
            else:
                commands_exe.get(cmd_input)()

    def add(self):
        """
        Добавление нового рейса в список рейсов.
        :return:
        """
        print('\nВведите данные рейса:')
        flight_number = input('XXXХ - номер рейса: ').upper().strip()
        flight_number = self.validate.flight_num_input(flight_number)

        departure_date = input('ДД/ММ/ГГГГ - дата рейса: ').upper().strip()
        departure_date = self.validate.date_input(departure_date)

        departure_time = input('ЧЧ:ММ - время вылета: ').upper().strip()
        departure_time = self.validate.time_input(departure_time)

        flight_duration = input('ЧЧ.ММ - длительность полёта: ').upper().strip()
        flight_duration = self.validate.flight_duration_input(flight_duration)

        departure_airport_code = input('XXX - аэропорт вылета: ').upper().strip()
        departure_airport_code = self.validate.airport_code_input(departure_airport_code)

        arrival_airport_code = input('XXX - аэропорт назначения: ').upper().strip()
        arrival_airport_code = self.validate.airport_code_input(arrival_airport_code)

        ticket_price = input('.XX - стоимость билета: ').strip()
        ticket_price = self.validate.ticket_price_input(ticket_price)

        flight_to_add = self.flight(flight_number,
                                    departure_date,
                                    departure_time,
                                    flight_duration,
                                    departure_airport_code,
                                    arrival_airport_code,
                                    ticket_price)
        self.controller.set_flight_list(flight_to_add)

        print('Добавлен рейс:\n{}'.format(flight_to_add))

    def search(self):
        """
        Поиск рейса в списке по номеру.
        :return: Нет
        """
        flight_number = input('Введите номер рейса в формате ХХХХ: ')
        flight_number = self.validate.flight_num_input(flight_number)
        flight = self.controller.search_flight(flight_number)
        if flight:
            print(flight)
        else:
            print('Рейс не найден!')

    def output(self):
        """
        Вывод всех рейсов из списка.
        :return:
        """
        if len(self.controller.get_flight_list()) != 0:
            for flight in self.controller.get_flight_list():
                print(flight)
        else:
            print('Список рейсов пуст!')
