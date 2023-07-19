from typing import List

from controller.flight import Flight
from model.rw_repository import RepoOperations


class UserController:
    """
    Обработка запросов и команд из пользовательского класса.
    Получение данных из репозитория, отправка данных в репозиторий.
    """
    def __init__(self):
        self.__repo_list = []
        self.repo_operations = RepoOperations()

    def get_flight_list(self) -> List[Flight]:
        return self.__repo_list

    def set_flight_list(self, new_flight: Flight):
        self.__repo_list.append(new_flight)

    def search_flight(self, flight_num) -> Flight:
        """
        Поиск рейса по номеру.
        :param flight_num:
        :return: Рейс
        """
        for flight in self.__repo_list:
            if flight_num == flight.flight_number:
                return flight

    def save_to_repo(self):
        """
        Сохранение списка рейсов в репозиторий.
        :return:
        """
        self.repo_operations.write_to_repo(self.__repo_list)

    def read_from_repo(self):
        """
        Создание списка рейсов, полученных из репозитория.
        :return:
        """
        data = self.repo_operations.read_from_repo()
        for item in data:
            self.__repo_list.append(Flight(flight_number=item.get('flight_number'),
                                           departure_date=item.get('departure_date'),
                                           departure_time=item.get('departure_time'),
                                           flight_duration=item.get('flight_duration'),
                                           departure_airport_code=item.get('departure_airport_code'),
                                           arrival_airport_code=item.get('arrival_airport_code'),
                                           ticket_price=item.get('ticket_price'))
                                    )
