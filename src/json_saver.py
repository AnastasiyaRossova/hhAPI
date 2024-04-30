import json
from abc import ABC, abstractmethod


class AbstractJSONSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        return None

    @abstractmethod
    def delete_vacancy(self, vacancy):
        return None

    @abstractmethod
    def commit(self, filename):
        return None


class JSONSaver(AbstractJSONSaver):

    def __init__(self):
        self._vacancies = []

    def add_vacancy(self, vacancy):
        self._vacancies.append(vacancy.json)

    def delete_vacancy(self, vacancy):
        self._vacancies.remove(vacancy.json)

    def commit(self, filename):
        with open(f"data/{filename}.json", 'w') as f:
            f.write(json.dumps(self._vacancies))