import pytest
from src.hh import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver



@pytest.fixture()
def headHunterAPI_object():
    return HeadHunterAPI()


@pytest.fixture()
def vacancy_object():
    return Vacancy(
        "123", 100, 1000, "Программист", {},
        "Yandex", "Уметь сидеть на стуле",
        """{"id": "123", "salary": {"to": 1000, "from": 100}, "name": "\\u041f\\u0440\\u043e\\u0433\\u0440\\u0430\\u043c\\u043c\\u0438\\u0441\\u0442", "employer": {"name": "Yandex"}}"""    )


@pytest.fixture()
def jSONSaver_object():
    return JSONSaver()


def test_cast_to_object_list(vacancy_object):
    vacancies = [{
        "id": "123",
        "salary": {
            "to": 1000,
            "from": 100,
        },
        "name": "Программист",
        "employer": {"name": "Yandex"},
    }]
    assert [vacancy_object] == Vacancy.cast_to_object_list(vacancies)
