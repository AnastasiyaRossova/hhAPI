import json
from abc import ABC, abstractmethod


class AbstractJSONSaver(ABC):
    """
    Абстрактный класс для json
    """
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
    """
    Класс для json
    """
    def __init__(self):
        self._vacancies = []

    def add_vacancy(self, vacancy):
        """Добавить вакансию"""
        self._vacancies.append(vacancy.json)

    def delete_vacancy(self, vacancy):
        """Убрать вакансию"""
        self._vacancies.remove(vacancy.json)

    def commit(self, filename):
        """Сохранить вакансии в фаил"""
        with open(f"data/{filename}.json", 'w') as f:
            f.write(json.dumps(self._vacancies))