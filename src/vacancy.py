from abc import ABC, abstractmethod


class AbstractVacancy(ABC):
    @abstractmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list:
        return None


class Vacancy:
    def __init__(self, _id, salary_from, salary_to, name, area,
                 employer_name, requirement, json):
        self._id = _id
        self._salary_from = salary_from
        self._salary_to = salary_to
        self._name = name
        self._area = area
        self._employer_name = employer_name
        self._requirement = requirement
        self._json = json

    @property
    def json(self) -> str:
        return self._json

    @property
    def name(self) -> str:
        return self._name

    @property
    def salary_to(self) -> str:
        return self._salary_to

    def __repr__(self):
        return f'Вакансия [{self._id}] {self._name}: {self._name}'

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self._salary_to == other._salary_to

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list:
        vacancies_list = []
        for vacancy in vacancies:
            new_vacancy = Vacancy(
                vacancy.get("_id"),
                vacancy.get("salary").get("from") if vacancy.get("salary") else "",
                vacancy.get("salary").get("to") if vacancy.get("salary") else "",
                vacancy.get("name"),
                vacancy.get("area"),
                vacancy.get("employer").get("name") if vacancy.get("employer") else "",
                vacancy.get("requirement") if vacancy.get("requirement") else "",
                vacancy
            )
            vacancies_list.append(new_vacancy)
        return vacancies_list
