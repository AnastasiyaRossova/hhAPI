from abc import ABC, abstractmethod


class AbstractVacancy(ABC):
    @abstractmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list:
        return None


class Vacancy:
    def __init__(self, _id, salary, name, area, employer_name, requirement, json):
        self._id = _id
        self._salary = salary
        self._name = name
        self._area = area
        self._employer_name = employer_name
        self._requirement = requirement
        self._json = json

    def __repr__(self):
        return f'Вакансия [{self._id}] {self._name}: {self._name}'

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list:
        vacancies_list = []
        for vacancy in vacancies:
            new_vacancy = Vacancy(
                vacancy.get("_id"),
                vacancy.get("salary"),
                vacancy.get("name"),
                vacancy.get("area"),
                vacancy.get("employer").get("name"),
                vacancy.get("requirement") if vacancy.get("requirement") else "",
                vacancy
            )
        vacancies_list.append(new_vacancy)
        return vacancies_list
