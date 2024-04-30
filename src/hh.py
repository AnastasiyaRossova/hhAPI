from abc import ABC, abstractmethod

import requests


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        return None


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """Загрузить вакансии"""
        self.params['text'] = keyword
        while self.params.get('page') != 2:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json().get('items')
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
