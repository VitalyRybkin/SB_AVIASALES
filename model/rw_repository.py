import json
from typing import List

from controller.flight import Flight


class RepoOperations:
    """
    Запись и чтение информации из репозитория.
    """
    def __init__(self):
        self.__file_name = 'repository.json'

    def read_from_repo(self) -> dict:
        """
        Чтение из репозитория.
        :return: Список словарей репозитория.
        """
        try:
            with open(self.__file_name, 'r') as repo:
                data = json.load(repo)
        except FileExistsError:
            print('Execution error: repository file does not exists!')
        return data

    def write_to_repo(self, repo_list: List[Flight]):
        """
        Запись списка словарей с информацией о рейсах в репозиторий.
        :param repo_list: Список рейсов.
        """
        flights_to_save_to_repo = list()
        flights = dict()
        for flight in repo_list:
            for attribute, value in flight.__dict__.items():
                flights[attribute] = value
            flights_to_save_to_repo.append(flights.copy())
            flights.clear()

        try:
            with open(self.__file_name, 'w') as repo:
                json.dump(flights_to_save_to_repo, repo, indent=4)
        except FileExistsError:
            print('Execution error: repository file does not exists!')
